import os
import asyncio
from pathlib import Path
import pysrt
import tqdm.asyncio
from deep_translator import GoogleTranslator
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Defina o caminho das pastas
pasta_legendas_originais = './legendas/legendas_originais/'
pasta_legendas_traduzidas = './legendas/legendas_traduzidas/'
pasta_legendas = './legendas/'

# Crie as pastas caso elas não existam
if not os.path.exists(pasta_legendas_originais):
    os.makedirs(pasta_legendas_originais)

if not os.path.exists(pasta_legendas_traduzidas):
    os.makedirs(pasta_legendas_traduzidas)

if not os.path.exists(pasta_legendas):
    os.makedirs(pasta_legendas)

# Função para obter os idiomas alvo do usuário
def get_target_languages():
    print("Digite os códigos dos idiomas para os quais você deseja traduzir, separados por vírgula.")
    print("Exemplo: pt,en,es,ar")
    user_input = input("Idiomas alvo: ").strip()
    return [lang.strip() for lang in user_input.split(',') if lang.strip()]

# Obter idiomas alvo do usuário
target_languages = get_target_languages()

# Configurações de tradução
sentence_endings = ['.', '!', '?', ')', 'よ', 'ね', 'の', 'さ', 'ぞ', 'な', 'か', '！', '。', '」', '…']
separator = " ◌ "
separator_unjoin = separator.replace(' ', '')
chunk_max_chars = 4999

def join_sentences(lines, max_chars):
    joined_lines = []
    current_chunk = ""

    for line in lines:
        if not line or line is None:
            line = 'ㅤ'

        if len(current_chunk) + len(line) + len(separator) <= max_chars:
            current_chunk += line + separator
            if any(line.endswith(ending) for ending in sentence_endings):
                joined_lines.append(current_chunk)
                current_chunk = ""
        else:
            if current_chunk:
                joined_lines.append(current_chunk)
                current_chunk = ""
            if len(current_chunk) + len(line) + len(separator) <= max_chars:
                current_chunk += line + separator
            else:
                end_index = line.rfind(' ', 0, max_chars - (1 + len(separator)))
                if end_index == - (1 + len(separator)):
                    end_index = max_chars - (1 + len(separator))
                joined_lines.append((line[:end_index] + '…' + separator)[:max_chars])

    if current_chunk:
        joined_lines.append(current_chunk)

    return joined_lines

def split_subtitle(text, max_lines=2):
    words = text.split()
    if len(words) <= max_lines:
        return text

    lines = []
    words_per_line = len(words) // max_lines
    remainder = len(words) % max_lines

    start = 0
    for i in range(max_lines):
        end = start + words_per_line + (1 if i < remainder else 0)
        lines.append(' '.join(words[start:end]))
        start = end

    return '\n'.join(lines)

def unjoin_sentences(original_sentence: str, modified_sentence: str, separator: str):
    if original_sentence is None:
        return ' '

    original_lines = original_sentence.split(separator)
    original_lines = [s.strip() for s in original_lines if s.strip()]

    if modified_sentence is None:
        return original_lines or ' '

    modified_sentence = modified_sentence.replace(f"{separator_unjoin} ", f"{separator_unjoin}").replace(f" {separator_unjoin}", f"{separator_unjoin}").replace(
        f"{separator_unjoin}.", f".{separator_unjoin}").replace(f"{separator_unjoin},", f",{separator_unjoin}")

    modified_lines = modified_sentence.split(separator_unjoin)
    modified_lines = [s.strip() for s in modified_lines if s.strip()]

    if original_lines == "..." or original_lines == "…":
        return original_lines

    if len(original_lines) == len(modified_lines):
        return modified_lines

    original_word_count = sum(len(line.split()) for line in original_lines)
    modified_word_count = len(' '.join(modified_lines).split())
    
    if original_word_count == 0 or modified_word_count == 0:
        return original_sentence.replace(separator, ' ').strip()

    modified_words_proportion = modified_word_count / original_word_count
    modified_words = ' '.join(modified_lines).split()

    new_modified_lines = []
    current_index = 0

    for original_line in original_lines:
        num_words = max(1, int(round(len(original_line.split()) * modified_words_proportion)))
        line_words = modified_words[current_index:current_index + num_words]
        new_modified_lines.append(' '.join(line_words))
        current_index += num_words

    if current_index < len(modified_words):
        new_modified_lines[-1] += ' ' + ' '.join(modified_words[current_index:])

    return new_modified_lines or original_lines or ' '

async def translate_chunk(index, chunk, target_lang):
    while True:
        try:
            translator = GoogleTranslator(source='auto', target=target_lang)
            translated_chunk = await asyncio.get_event_loop().run_in_executor(None, translator.translate, chunk)
            await asyncio.sleep(0)

            if translated_chunk is None or len(translated_chunk.replace(separator.strip(), '').split()) == 0:
                return chunk

            return translated_chunk
        except Exception as e:
            print(f"\r[chunk {index}]: Exception: {e.__doc__} Retrying in 30 seconds...", flush=True)
            await asyncio.sleep(30)

async def translate_srt_file(srt_file_path: Path, translated_subtitle_path: Path, target_lang):
    subs = pysrt.open(srt_file_path, encoding='utf-8')
    sub_content = [' '.join(sub.text.strip().splitlines()) for sub in subs]
    chunks = join_sentences(sub_content, chunk_max_chars) or []
    translated_chunks = [None] * len(chunks)

    tasks = []
    semaphore = asyncio.Semaphore(7)

    async def translate_async():
        async def run_translate(index, chunk, lang):
            while True:
                try:
                    async with semaphore:
                        result = await asyncio.wait_for(translate_chunk(index, chunk, lang), 120)
                    translated_chunks[index] = result
                    break
                except Exception:
                    await asyncio.sleep(3)

        for index, chunk in enumerate(chunks):
            task = asyncio.create_task(run_translate(index, chunk, target_lang))
            tasks.append(task)

        for tsk in tqdm.asyncio.tqdm.as_completed(tasks, total=len(tasks), desc="Translating", unit="chunks", unit_scale=False, leave=True, bar_format="{desc} {percentage:3.0f}% | {n_fmt}/{total_fmt} | ETA: {remaining} | ⏱: {elapsed}"):
            await tsk

    await translate_async()

    print('Processing translation...', end='')

    unjoined_texts = [unjoin_sentences(chunk, translated_chunks[i], separator_unjoin) or "" for i, chunk in enumerate(chunks)]
    unjoined_texts = [text for sublist in unjoined_texts for text in sublist]

    for i, segment in enumerate(unjoined_texts):
        unjoined_texts[i] = split_subtitle(segment, max_lines=len(subs[i].text.splitlines())) 

    for i, sub in enumerate(subs):
        sub.text = unjoined_texts[i]

    os.makedirs(translated_subtitle_path.parent, exist_ok=True)
    subs.save(translated_subtitle_path, encoding='utf-8')

    print('\r                         ', end='\r')

    return subs

async def main():
    original_folder = Path(pasta_legendas_originais)
    translated_folder = Path(pasta_legendas_traduzidas)

    os.makedirs(translated_folder, exist_ok=True)

    for filename in os.listdir(original_folder):
        if filename.endswith('.srt'):
            for lang in target_languages:
                input_file_path = original_folder / filename
                output_filename = f'{filename[:-4]}_{lang}.srt'
                output_file_path = translated_folder / output_filename
                
                if not output_file_path.exists():
                    print(f'Traduzindo para {lang}: {filename}')
                    await translate_srt_file(input_file_path, output_file_path, lang)

    print('Traduções concluídas.')

if __name__ == "__main__":
    asyncio.run(main())
