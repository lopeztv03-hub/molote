@echo off
REM Real TikTok API Setup and Run Launcher

cd /d "%~dp0"

echo.
echo ================================================================================
echo.
echo   🎬 TIKTOK BOT - REAL HEARTS SETUP AND RUN
echo.
echo ================================================================================
echo.
echo What would you like to do?
echo.
echo 1. Setup TikTok API (interactive guide)
echo 2. Verify setup is complete
echo 3. Run bot with real hearts
echo 4. Run demo (mock API - no setup needed)
echo 5. Exit
echo.

set /p choice="Enter your choice (1-5): "

if "%choice%"=="1" goto setup
if "%choice%"=="2" goto verify
if "%choice%"=="3" goto run
if "%choice%"=="4" goto demo
if "%choice%"=="5" goto end

echo Invalid choice. Please try again.
goto end

:setup
echo.
echo Starting interactive setup guide...
echo.
python SETUP_GUIDE.py
pause
goto end

:verify
echo.
echo Verifying setup...
echo.
python VERIFY_SETUP.py
pause
goto end

:run
echo.
echo Running bot with REAL TikTok API...
echo.
python full_auto_bot.py
pause
goto end

:demo
echo.
echo Running demo with MOCK API (no setup needed)...
echo.
python quickstart.py
pause
goto end

:end
