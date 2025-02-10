@echo off
python py/main.py %1

if %ERRORLEVEL% neq 0 (
    echo:
    echo:
    echo Python script encountered an error.
    echo:
    exit /b 1
)

lilypond -o pdf/%1 ly/main.ly