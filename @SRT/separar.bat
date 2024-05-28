@echo off
for /r %%a in (*.srt) do (
    python srtGD.py "%%a"
)