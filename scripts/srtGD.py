import pysrt
import argparse

# Defina o comprimento máximo de linha desejado
MAX_LINE_LENGTH = 42

# Função para quebrar uma linha longa em várias linhas
def wrap_line(line, max_length):
    words = line.split()
    wrapped_lines = []
    current_line = ''

    for word in words:
        if len(current_line) + len(word) + (1 if current_line else 0) <= max_length:  # Adiciona 1 por causa do espaço
            if current_line:
                current_line += ' ' + word
            else:
                current_line = word
        else:
            wrapped_lines.append(current_line)
            current_line = word

    if current_line:
        wrapped_lines.append(current_line)

    return '\n'.join(wrapped_lines)

# Função para dividir uma legenda em várias partes se necessário
def split_subtitle(sub, wrapped_text):
    lines = wrapped_text.split('\n')
    lines = [line for line in lines if line.strip()]  # Remove linhas em branco geradas durante a quebra

    if len(lines) <= 2:
        sub.text = wrapped_text
        return [sub]  # Não precisa dividir

    parts = []
    current_start = sub.start
    start_ms = sub.start.ordinal
    end_ms = sub.end.ordinal
    duration_per_line = (end_ms - start_ms) // len(lines)

    for i in range(0, len(lines), 2):
        part_lines = lines[i:i + 2]
        part_text = '\n'.join(part_lines)
        
        part_end_ms = start_ms + duration_per_line * min(i + 2, len(lines))
        part_end = pysrt.SubRipTime.from_ordinal(part_end_ms)
        
        new_sub = pysrt.SubRipItem(index=sub.index, start=current_start, end=part_end, text=part_text)
        parts.append(new_sub)
        
        current_start = part_end

    return parts

def main(args):
    # Carregue o arquivo SRT
    subs = pysrt.open(args.input_file)

    new_subs = pysrt.SubRipFile()

    # Percorra todas as legendas
    for sub in subs:
        # Quebre as linhas longas do texto, preservando quebras de linha existentes
        lines = sub.text.split('\n')
        wrapped_lines = [wrap_line(line, MAX_LINE_LENGTH) for line in lines]
        wrapped_text = '\n'.join(wrapped_lines)

        # Dividir a legenda se necessário
        split_parts = split_subtitle(sub, wrapped_text)
        
        # Adicionar as partes divididas ao novo conjunto de legendas
        new_subs.extend(split_parts)

    # Ajustar os índices das legendas no novo conjunto
    new_subs.clean_indexes()

    # Salve as legendas modificadas no arquivo original
    new_subs.save(args.input_file, encoding='utf-8')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Quebra de linhas e divisão de legendas em um arquivo SRT.')
    parser.add_argument('input_file', type=str, help='O caminho para o arquivo SRT de entrada')
    
    args = parser.parse_args()
    main(args)
