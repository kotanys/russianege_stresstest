@echo off
choice /m "������� ����?"
if %errorlevel% equ 1 ( python with_song.py ) else ( if %errorlevel% equ 2 ( python main.py ))
pause