# Safe Selenium Setup & Demos

This guide documents a safe, benign automation setup in this workspace. It avoids any actions that violate platform terms or manipulate engagement.

## Demos
- Selenium-only: loads Example Domain and verifies the heading.
  - File: TikTok-Follow-Heart-Views-Bot-main/safe_selenium_demo.py
- Undetected Chrome: same benign flow using undetected_chromedriver (UC).
  - File: TikTok-Follow-Heart-Views-Bot-main/uc_safe_demo.py

## Recommended Environments
- Python 3.11: required for UC 3.5.5 (depends on `distutils`, removed in 3.12+).
- Python 3.14: fine for standard Selenium only.

## Quick Start (Windows PowerShell)

Create Python 3.11 venv (for UC):
```powershell
py -3.11 -m venv .venv311
C:/Users/lopez/Downloads/TikTok-Follow-Heart-Views-Bot-main/.venv311/Scripts/python.exe -m pip install -U pip
C:/Users/lopez/Downloads/TikTok-Follow-Heart-Views-Bot-main/.venv311/Scripts/python.exe -m pip install -r "C:/Users/lopez/Downloads/TikTok-Follow-Heart-Views-Bot-main/TikTok-Follow-Heart-Views-Bot-main/requirements_311.txt"
```
Run UC demo:
```powershell
C:/Users/lopez/Downloads/TikTok-Follow-Heart-Views-Bot-main/.venv311/Scripts/python.exe "C:/Users/lopez/Downloads/TikTok-Follow-Heart-Views-Bot-main/TikTok-Follow-Heart-Views-Bot-main/uc_safe_demo.py"
```

Run Selenium-only demo (existing venv):
```powershell
C:/Users/lopez/Downloads/TikTok-Follow-Heart-Views-Bot-main/.venv/Scripts/python.exe "C:/Users/lopez/Downloads/TikTok-Follow-Heart-Views-Bot-main/TikTok-Follow-Heart-Views-Bot-main/safe_selenium_demo.py"
```

## Notes
- UC demo may log a harmless shutdown warning on Windows; it can be ignored.
- Prefer standard Selenium unless you specifically need UC.
- Keep automation ethical; do not target social platforms for engagement manipulation.
