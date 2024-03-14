@echo off
setlocal enabledelayedexpansion

set "background=background.mp3"
set "output_folder=mesclado"

if not exist "%output_folder%" mkdir "%output_folder%"

for %%a in (audios\*.mp3) do (
    set "input=%%a"
    set "output=!output_folder!\!input:audios\=!"
    set "output=!output:.mp3=(com background).mp3!"
    ffmpeg -i "%background%" -i "!input!" -filter_complex "[0:a] [1:a] amix=inputs=2:duration=longest" "!output!" -y
)

for %%a in (audios\*.wav) do (
    set "input=%%a"
    set "output=!output_folder!\!input:audios\=!"
    set "output=!output:.wav=(com background).wav!"
    ffmpeg -i "%background%" -i "!input!" -filter_complex "[0:a] [1:a] amix=inputs=2:duration=longest" "!output!" -y
)
pause