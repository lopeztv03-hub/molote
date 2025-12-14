#!/usr/bin/env python3
"""
TikTok OAuth Authorization
Get a real access token to post actual hearts to TikTok
"""

import os
import webbrowser
import json
from dotenv import load_dotenv
import requests

load_dotenv()

print("=" * 80)
print(" " * 20 + "🔐 TIKTOK OAUTH AUTHORIZATION")
print("=" * 80)
print()

client_key = os.getenv("TIKTOK_CLIENT_KEY")
client_secret = os.getenv("TIKTOK_CLIENT_SECRET")

if not client_key or not client_secret:
    print("❌ Error: Missing credentials in .env")
    print()
    print("Add these to .env file:")
    print("TIKTOK_CLIENT_KEY=your_key")
    print("TIKTOK_CLIENT_SECRET=your_secret")
    exit(1)

print("Your credentials loaded from .env ✓")
print()

# Step 1: Generate OAuth URL
print("=" * 80)
print("STEP 1: Generate Authorization URL")
print("=" * 80)
print()

redirect_uri = "http://localhost:8000/callback"
scope = "user.info.basic,video.list"

oauth_url = f"https://www.tiktok.com/oauth/authorize?client_key={client_key}&scope={scope}&response_type=code&redirect_uri={redirect_uri}"

print("📱 Click this link or copy it to your browser:")
print()
print(oauth_url)
print()

# Try to open browser
try:
    webbrowser.open(oauth_url)
    print("✓ Browser opened! Check for TikTok authorization popup.")
except:
    print("(Could not open browser - please copy the link above)")

print()
print("=" * 80)
print("STEP 2: Approve the App")
print("=" * 80)
print()

print("""
1. You'll see a TikTok login/approval screen
2. Log in with your TikTok account (the one with @cirumtv)
3. Click "Approve" or "Allow"
4. You'll be redirected to a page with a code
""")

print()
print("=" * 80)
print("STEP 3: Enter Your Authorization Code")
print("=" * 80)
print()

auth_code = input("📋 Paste the authorization code here: ").strip()

if not auth_code:
    print()
    print("❌ No code provided. Exiting.")
    exit(1)

print()
print("=" * 80)
print("STEP 4: Exchange Code for Access Token")
print("=" * 80)
print()

try:
    print("Contacting TikTok OAuth server...")
    
    # Exchange code for token
    token_url = "https://open.tiktokapis.com/v1/oauth/token"
    
    payload = {
        "client_key": client_key,
        "client_secret": client_secret,
        "code": auth_code,
        "grant_type": "authorization_code",
        "redirect_uri": redirect_uri
    }
    
    response = requests.post(token_url, json=payload)
    data = response.json()
    
    if response.status_code == 200 and "data" in data:
        access_token = data["data"].get("access_token")
        refresh_token = data["data"].get("refresh_token")
        expires_in = data["data"].get("expires_in")
        
        if access_token:
            print("✅ Authorization successful!")
            print()
            
            # Save to .env
            print("Saving access token to .env...")
            
            # Read current .env
            env_path = ".env"
            env_content = ""
            if os.path.exists(env_path):
                with open(env_path, "r") as f:
                    env_content = f.read()
            
            # Update or add tokens
            if "TIKTOK_ACCESS_TOKEN=" in env_content:
                env_content = env_content.replace(
                    [line for line in env_content.split("\n") if line.startswith("TIKTOK_ACCESS_TOKEN=")][0],
                    f"TIKTOK_ACCESS_TOKEN={access_token}"
                )
            else:
                env_content += f"\nTIKTOK_ACCESS_TOKEN={access_token}"
            
            if refresh_token:
                if "TIKTOK_REFRESH_TOKEN=" in env_content:
                    env_content = env_content.replace(
                        [line for line in env_content.split("\n") if line.startswith("TIKTOK_REFRESH_TOKEN=")][0],
                        f"TIKTOK_REFRESH_TOKEN={refresh_token}"
                    )
                else:
                    env_content += f"\nTIKTOK_REFRESH_TOKEN={refresh_token}"
            
            # Write back
            with open(env_path, "w") as f:
                f.write(env_content)
            
            print("✓ Saved to .env")
            print()
            print(f"Access Token: {access_token[:30]}...")
            print(f"Expires in: {expires_in} seconds")
            if refresh_token:
                print(f"Refresh Token: {refresh_token[:30]}...")
            print()
            print("=" * 80)
            print("✅ ALL SET!")
            print("=" * 80)
            print()
            print("Your bot can now post REAL hearts to TikTok!")
            print()
            print("Run the bot:")
            print("  python full_auto_bot.py")
            print()
        else:
            print("❌ No access token in response")
            print(f"Response: {data}")
    else:
        print(f"❌ Authorization failed!")
        print(f"Status: {response.status_code}")
        print(f"Response: {data}")
        print()
        print("Troubleshooting:")
        print("- Make sure you entered the correct authorization code")
        print("- Check that your app is configured as 'Web Application' in TikTok Dashboard")
        print("- Verify redirect URI is: http://localhost:8000/callback")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
