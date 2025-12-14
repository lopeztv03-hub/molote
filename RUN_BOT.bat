@echo off
REM TikTok Bot Launcher for Windows
REM Just double-click this file to run!

cd /d "%~dp0"

echo.
echo ========================================================
echo   🎬 TIKTOK BOT - CHOOSE MODE
echo ========================================================
echo.
echo 1 = Automatic (Recommended)
echo 2 = Interactive
echo 3 = Demo
echo 4 = Exit
echo.

set /p choice="Choose (1-4): "

if "%choice%"=="1" (
    echo.
    echo Starting Automatic Bot...
    echo.
    python full_auto_bot.py
    pause
) else if "%choice%"=="2" (
    echo.
    echo Starting Interactive Bot...
    echo.
    python standalone_bot.py
    pause
) else if "%choice%"=="3" (
    echo.
    echo Starting Demo Mode...
    echo.
    python video_watcher.py demo
    pause
) else if "%choice%"=="4" (
    echo Exiting...
    exit /b
) else (
    echo Invalid choice!
    pause
    goto start
)
