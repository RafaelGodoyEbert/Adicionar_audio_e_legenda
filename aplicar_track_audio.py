import os

# Diretório contendo os arquivos de áudio
diretorio = "áudios"

# Arquivo de vídeo original
video = 'video.mp4'

# FPS
fps_video = 30

# Qualidade de áudio
audio_kbps = 128

# Lista todos os arquivos no diretório
arquivos = os.listdir(diretorio)

# Lista de inputs para o comando ffmpeg
inputs = f'-i "{video}" '

# Lista de mapeamentos de áudio para o comando ffmpeg
mapeamento_audio = ''

# Contador para o número de faixas de áudio
contador_audio = 0

# Adiciona o mapeamento de áudio para o áudio original do vídeo
mapeamento_audio += f'-map 0:v '

# Adiciona o mapeamento de áudio para o áudio original do vídeo
mapeamento_audio += f'-map 0:a '

# Incrementa o contador de faixas de áudio
contador_audio += 1

# Loop pelos arquivos
for arquivo in arquivos:
    if arquivo.endswith('.mp3'):
        # Extrai o idioma do nome do arquivo
        idioma = arquivo.split(' - ')[-1].split('.')[0]
        
        # Adiciona o arquivo de áudio à lista de inputs e mapeamento de áudio
        inputs += f'-i "{os.path.join(diretorio, arquivo)}" '
        mapeamento_audio += f'-map {contador_audio}:a -metadata:s:a:{contador_audio - 1} language={idioma} '
        
        # Incrementa o contador de faixas de áudio
        contador_audio += 1

# Comando ffmpeg para combinar o vídeo original e as faixas de áudio adicionais
comando_ffmpeg = f'ffmpeg {inputs} {mapeamento_audio}-r {fps_video} -c:v copy -c:a aac -b:a {audio_kbps}k output-track.mp4'

# Executa o comando ffmpeg
os.system(comando_ffmpeg)
