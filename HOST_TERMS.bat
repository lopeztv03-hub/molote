@echo off
REM Simple local host for Terms and Privacy pages
cd /d "%~dp0"

REM Ensure index exists
if not exist index.html (
  echo Creating index.html to route to terms_of_service.html
  echo ^<meta http-equiv="refresh" content="0; url=terms_of_service.html" /^> > index.html
)

REM Start local server on port 8080
where python >nul 2>&1
if errorlevel 1 (
  echo Python not found in PATH. Please run with your venv:
  echo   "%~dp0\.venv\Scripts\python.exe" -m http.server 8080
  goto :end
)

python -m http.server 8080

:end
pause
