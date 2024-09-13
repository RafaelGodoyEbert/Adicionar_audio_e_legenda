@echo off
call venv/scripts/activate
set backup_dir=backup/backup_legendas

rem Cria os diretórios de backup se não existirem
if not exist "%backup_dir%\legendas_originais" mkdir "%backup_dir%\legendas_originais"
if not exist "%backup_dir%\legendas_traduzidas" mkdir "%backup_dir%\legendas_traduzidas"

rem Copia todos os arquivos .srt para o diretório de backup
for /r "legendas\legendas_originais" %%a in (*.srt) do (
    copy "%%a" "%backup_dir%\legendas_originais"
    python scripts\srtGD.py "%%a"
)

for /r "legendas\legendas_traduzidas" %%a in (*.srt) do (
    copy "%%a" "%backup_dir%\legendas_traduzidas"
    python scripts\srtGD.py "%%a"
)

echo Backup concluído.
pause
