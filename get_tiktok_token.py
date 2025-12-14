#!/usr/bin/env python3
"""
TikTok OAuth Authorization
Get access token so the bot can post REAL hearts
"""

import os
import webbrowser
from dotenv import load_dotenv
from src.tiktok_api import TikTokAPI

load_dotenv()

print("=" * 70)
print("🔐 TIKTOK OAUTH AUTHORIZATION")
print("=" * 70)
print()

# Initialize API
api = TikTokAPI(
    client_key=os.getenv("TIKTOK_CLIENT_KEY"),
    client_secret=os.getenv("TIKTOK_CLIENT_SECRET")
)

print("Step 1: Generate OAuth URL")
print()

# Generate OAuth URL
oauth_url = api.get_oauth_url(
    redirect_uri="http://localhost:8000/callback",
    scope="user.info.basic,video.list"
)

print(f"OAuth URL: {oauth_url}")
print()

print("Step 2: Open in browser and approve")
print()

# Try to open browser
try:
    webbrowser.open(oauth_url)
    print("✓ Browser opened (check for permission request)")
except:
    print(f"Please copy and paste this URL in your browser:")
    print(oauth_url)

print()

# Get authorization code
print("Step 3: After approval, you'll see a code")
print()

auth_code = input("Paste the authorization code here: ").strip()

if not auth_code:
    print("❌ No code provided")
    exit(1)

print()
print("Step 4: Exchange code for access token")
print()

# Exchange code for token
try:
    result = api.exchange_code_for_token(
        code=auth_code,
        redirect_uri="http://localhost:8000/callback"
    )
    
    if result:
        print("✓ Authorization successful!")
        print()
        print("Access token received. Your bot can now post REAL hearts!")
        print()
        print("Run the bot:")
        print("  python full_auto_bot.py")
        print()
    else:
        print("❌ Authorization failed")
        print("Check your code and try again")
        
except Exception as e:
    print(f"❌ Error: {e}")
    print()
    print("Possible issues:")
    print("- Wrong authorization code")
    print("- OAuth not set up in TikTok Dashboard")
    print("- Try running the bot directly (it will generate the URL)")
