import os
import subprocess
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Defina o caminho para o vídeo e a pasta de legendas
print("Selecione o nome do vídeo:")
video_path = './' + input("Digite o nome do arquivo de vídeo: ")  # Referenciando o vídeo na pasta pai
output_path = f'./{os.path.splitext(os.path.basename(video_path))[0]}_sub_track.mp4'

# Crie a pasta de saída caso ela não exista
output_folder = os.path.dirname(output_path)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Define o idioma padrão para as faixas de legenda
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

# Definir extensões de legenda suportadas
supported_subtitle_extensions = ['.srt', '.ass', '.vtt', '.sub']

# Solicitar input do usuário sobre a origem das legendas
print("Selecione a origem das legendas:")
print("1. Legendas originais")
print("2. Legendas traduzidas")
choice = input("Digite o número da opção desejada: ")

subtitle_folder = './legendas/legendas_originais' if choice == "1" else './legendas/legendas_traduzidas'

# Listar arquivos de legenda com qualquer uma das extensões suportadas
subtitle_files = [f for f in os.listdir(subtitle_folder) if os.path.splitext(f)[1] in supported_subtitle_extensions]

# Verificar se há arquivos de legenda
if not subtitle_files:
    raise ValueError("Nenhum arquivo de legenda encontrado na pasta especificada.")

# Construir listas de entradas e mapeamentos
input_files = ["-i", video_path]  # Começa com o vídeo
map_args = ['-map', '0:v', '-map', '0:a']  # Mapeia o vídeo e o áudio do arquivo 0
metadata_args = []

# Adicionar o áudio original como a faixa padrão
metadata_args.append('-metadata:s:a:0')
metadata_args.append('title="original"')
metadata_args.append('-metadata:s:a:0')
metadata_args.append(f'language="{default_language}"')

# Adicionar arquivos de legenda adicionais
for idx, subtitle_file in enumerate(subtitle_files):
    subtitle_path = os.path.join(subtitle_folder, subtitle_file).replace('\\', '/')  # Corrigir barras invertidas
    track_name = os.path.splitext(subtitle_file)[0]  # Nome do arquivo sem extensão
    # Usar o nome completo do idioma se estiver no mapeamento
    language_name = language_names.get(track_name, track_name)
    input_files.extend(["-i", subtitle_path])
    map_args.extend(["-map", f"{idx + 1}:s"])
    metadata_args.extend([
        f'-metadata:s:s:{idx}', f'title="{language_name}"',
        f'-metadata:s:s:{idx}', f'language="{track_name}"',
        f'-disposition:s:{idx}', '0'  # Definir disposição como 0 (não padrão) para todas as legendas
    ])

# Construir o comando ffmpeg
command = (
    ['ffmpeg'] +
    input_files +
    map_args +
    metadata_args +
    ['-c:v', 'copy', '-c:a', 'copy', '-c:s', 'mov_text', '-shortest', output_path]
)

# Exibir comando para depuração
command_str = ' '.join(command)
print(f"Executando comando: {command_str}")

# Executar o comando ffmpeg
result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# Exibir saída e erros do comando
print(result.stdout)
print(result.stderr)