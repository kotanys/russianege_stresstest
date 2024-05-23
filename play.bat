@echo off
chcp 65001 >nul
choice /m "Включить музыку?"
if %errorlevel% equ 1 ( python with_song.py ) else ( if %errorlevel% equ 2 ( python main.py ))
pause