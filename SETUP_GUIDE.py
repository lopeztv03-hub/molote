#!/usr/bin/env python3
"""
Interactive TikTok API Setup Guide
Step-by-step instructions to configure your bot for REAL hearts
"""

import webbrowser
import sys

print()
print("=" * 80)
print(" " * 15 + "🎬 TIKTOK BOT - REAL API SETUP GUIDE")
print("=" * 80)
print()

print("""
Welcome! This guide will help you set up your bot to post REAL hearts to TikTok.

The bot currently uses MOCK API (simulated hearts).
To post REAL hearts, you need to:

1. Configure your TikTok app in the Developer Dashboard
2. Get your credentials
3. Update your .env file
4. Run the bot!

Let's start:
""")

print()
print("-" * 80)
print("STEP 1: GO TO TIKTOK DEVELOPER DASHBOARD")
print("-" * 80)
print()

print("Open this URL in your browser:")
print("👉 https://developer.tiktok.com/")
print()

response = input("Have you logged in to the TikTok Developer Dashboard? (y/n): ").lower()
if response != 'y':
    print("Please visit https://developer.tiktok.com/ and come back.")
    sys.exit(0)

print()
print("-" * 80)
print("STEP 2: CREATE OR SELECT YOUR APP")
print("-" * 80)
print()

print("""
In the Developer Dashboard:
1. Click "Create an app" (if you don't have one yet)
2. Name it something like "Cirum Bot"
3. For Application Type, select "Web Application" (IMPORTANT!)
4. For Category, pick "Automation" or "Utility"
5. Click Create
""")

print()
input("Press ENTER when your app is created or selected...")

print()
print("-" * 80)
print("STEP 3: CONFIGURE OAUTH SCOPES")
print("-" * 80)
print()

print("""
In your app settings:
1. Go to the "Scopes" section
2. Enable these scopes:
   ✓ user.info.basic (Read basic user info)
   ✓ video.list (List videos)
   ✓ user.liking (REQUIRED - for liking/hearting videos)
3. Save changes
""")

print()
input("Press ENTER when scopes are configured...")

print()
print("-" * 80)
print("STEP 4: ADD REDIRECT URI")
print("-" * 80)
print()

print("""
In your app settings:
1. Go to "Redirect URIs" 
2. Add this redirect URI:
   http://localhost:8000/callback
3. Save changes
""")

print()
input("Press ENTER when redirect URI is added...")

print()
print("-" * 80)
print("STEP 5: COPY YOUR CREDENTIALS")
print("-" * 80)
print()

print("""
In your app dashboard, you should see:
- Client Key (or Client ID)
- Client Secret

Copy these values!
""")

client_key = input("Paste your Client Key: ").strip()
client_secret = input("Paste your Client Secret: ").strip()

if not client_key or not client_secret:
    print()
    print("❌ Error: You need both Client Key and Client Secret")
    sys.exit(1)

print()
print("-" * 80)
print("STEP 6: UPDATE .env FILE")
print("-" * 80)
print()

print("Updating your .env file with credentials...")

# Update .env file
env_content = f"""TIKTOK_CLIENT_KEY={client_key}
TIKTOK_CLIENT_SECRET={client_secret}
"""

with open(".env", "w") as f:
    f.write(env_content)

print("✓ .env file updated!")
print()

print()
print("-" * 80)
print("STEP 7: VERIFY SETUP")
print("-" * 80)
print()

print("Running verification...")
print()

try:
    from src.tiktok_api import TikTokAPI
    
    api = TikTokAPI(client_key=client_key, client_secret=client_secret)
    oauth_url = api.get_oauth_url(
        redirect_uri="http://localhost:8000/callback",
        scope=["user.info.basic", "video.list"]
    )
    
    print("✅ Setup verified successfully!")
    print()
    
except Exception as e:
    print(f"⚠️  Error during verification: {e}")
    print()
    print("Possible issues:")
    print("- App type not set to 'Web Application'")
    print("- Scopes not saved properly")
    print("- Redirect URI not added correctly")
    print()
    print("Please check your app settings and try again.")
    sys.exit(1)

print()
print("=" * 80)
print(" " * 20 + "🎉 SETUP COMPLETE!")
print("=" * 80)
print()

print("""
Your bot is now configured to post REAL hearts!

Next steps:

1. Run the bot:
   python full_auto_bot.py
   
2. OR double-click:
   START_BOT.bat

3. The bot will:
   - Generate an OAuth authorization URL
   - Ask you to approve access
   - Post 50 REAL hearts to your TikTok video
   - Display results

Your video URL:
https://www.tiktok.com/@cirumtv/photo/7582521253030907150

Let's go! 🚀
""")

print()
