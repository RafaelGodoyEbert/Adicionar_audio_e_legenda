import os
import subprocess
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Defina o caminho para o vídeo e a pasta de áudios
print("Selecione o nome do vídeo:")
video_path = './' + input("Digite o nome do arquivo de vídeo: ") 
audio_folder = "./audio_idiomas/"
output_path = f'./{os.path.splitext(video_path)[0]}_track.mp4'

# Crie a pasta de saída caso ela não exista
output_folder = os.path.dirname(output_path)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define o idioma padrão para as faixas adicionais
default_language = 'ptBR'

# Mapeamento de IDs de idioma para seus nomes completos
language_names = {
    'ptBR': 'Portuguese Brazil',
    'pt': 'Portuguese',
    'es': 'Spanish',
    'en': 'English',
    'fr': 'French',
    'de': 'German',
    'it': 'Italian',
    'ja': 'Japanese',
    'ru': 'Russian',
    'tr': 'Turkish',
    'hi': 'Hindi'
}

# Definir extensões de áudio suportadas
supported_extensions = ['.mp3', '.wav', '.aac', '.flac', '.ogg', '.m4a']

# Listar arquivos de áudio com qualquer uma das extensões suportadas
audio_files = [f for f in os.listdir(audio_folder) if os.path.splitext(f)[1] in supported_extensions]

# Verificar se há arquivos de áudio
if not audio_files:
    raise ValueError("Nenhum arquivo de áudio encontrado na pasta especificada.")

# Construir listas de entradas e mapeamentos
input_files = [f'-i "{video_path}"']  # Começa com o vídeo, entre aspas
map_args = ['-map 0:v']  # Mapeia o vídeo do arquivo 0
metadata_args = []

# Adicionar o áudio original como a faixa padrão
map_args.append('-map 0:a')
metadata_args.append('-metadata:s:a:0 title="original"')
metadata_args.append('-metadata:s:a:0 language="{}"'.format(default_language))

# Adicionar arquivos de áudio adicionais
for idx, audio_file in enumerate(audio_files):
    audio_path = os.path.join(audio_folder, audio_file).replace('\\', '/')  # Corrigir barras invertidas
    track_name = os.path.splitext(audio_file)[0]  # Nome do arquivo sem extensão
    # Usar o nome completo do idioma se estiver no mapeamento
    language_name = language_names.get(track_name, track_name)
    input_files.append(f'-i "{audio_path}"')  # Envolver o caminho de áudio em aspas
    map_args.append(f'-map {idx + 1}:a')
    metadata_args.append(f'-metadata:s:a:{idx + 1} title="{language_name}"')
    metadata_args.append(f'-metadata:s:a:{idx + 1} language="{track_name}"')

# Construir o comando ffmpeg
command = (
    ['ffmpeg'] +
    input_files +
    map_args +
    metadata_args +
    ['-c:v', 'copy', '-c:a', 'aac', '-shortest', f'"{output_path}"']  # Envolver o caminho de saída em aspas
)

# Exibir comando para depuração
command_str = ' '.join(command)
print(f"Executando comando: {command_str}")

# Executar o comando ffmpeg
result = subprocess.run(command_str, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Exibir saída e erros do comando
print(result.stdout)
print(result.stderr)
