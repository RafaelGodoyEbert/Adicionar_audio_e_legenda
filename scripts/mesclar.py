import os
import subprocess
import shutil

# Definir caminho absoluto para as pastas
audio_idiomas_folder = os.path.abspath('audio_idiomas')
audio_idiomas_backup_folder = os.path.abspath('./backup/audio_idiomas_backup')
background_audio = os.path.abspath('background.mp3')

def run_ffmpeg(input_audio, output_audio):
    command = [
        'ffmpeg', '-i', background_audio, '-i', input_audio,
        '-filter_complex', '[1:a]volume=2[a];[0:a][a]amix=inputs=2:duration=longest',
        output_audio, '-y'
    ]
    subprocess.run(command, check=True)

def process_audio_files():
    # Criar pasta de backup se não existir
    if not os.path.exists(audio_idiomas_backup_folder):
        os.makedirs(audio_idiomas_backup_folder)
        print(f"Pasta de backup criada: {audio_idiomas_backup_folder}")
    else:
        print(f"Pasta de backup já existe: {audio_idiomas_backup_folder}")

    # Fazer backup da pasta de áudios
    for root, dirs, files in os.walk(audio_idiomas_folder):
        for file in files:
            shutil.copy2(os.path.join(root, file), audio_idiomas_backup_folder)

    # Mesclar áudios
    for root, dirs, files in os.walk(audio_idiomas_backup_folder):
        for file in files:
            if file.endswith(('.mp3', '.wav')):
                input_audio = os.path.join(root, file)
                output_audio = os.path.join(audio_idiomas_folder, file)
                run_ffmpeg(input_audio, output_audio)

    print("Processamento concluído")

# Executar o processamento
process_audio_files()