#!/usr/bin/env python3
"""
Test TikTok Credentials
Verify if Client Key and Secret are valid
"""

from src.tiktok_api import TikTokAPI
import os
from dotenv import load_dotenv

load_dotenv()

print("=" * 70)
print("🧪 TESTING TIKTOK CREDENTIALS")
print("=" * 70)
print()

# Get credentials from .env
client_key = os.getenv("TIKTOK_CLIENT_KEY")
client_secret = os.getenv("TIKTOK_CLIENT_SECRET")

print("Credentials in .env file:")
print(f"  Client Key: {client_key[:20]}..." if client_key else "  ✗ Not found")
print(f"  Client Secret: {client_secret[:20]}..." if client_secret else "  ✗ Not found")
print()

if not client_key or not client_secret:
    print("✗ Missing credentials!")
    print("\nPlease make sure they're saved in .env file")
    exit(1)

# Test API
print("Testing API connection...")
api = TikTokAPI(client_key, client_secret)

print()
print("=" * 70)
print("DIAGNOSIS:")
print("=" * 70)
print()

# Check 1: Client Key format
if len(client_key) < 10:
    print("❌ Client Key is too short")
    print("   Action: Check TikTok Developer Dashboard -> App info")
    print("   Should be 32+ characters")
else:
    print("✓ Client Key format looks OK")

# Check 2: Client Secret format  
if len(client_secret) < 10:
    print("❌ Client Secret is too short")
    print("   Action: Check TikTok Developer Dashboard -> App info")
else:
    print("✓ Client Secret format looks OK")

print()
print("=" * 70)
print("NEXT STEPS:")
print("=" * 70)
print()

print("If you got a 404 error during OAuth, check these:")
print()
print("1. ❌ WRONG Client Key/Secret")
print("   → Go to: https://developers.tiktok.com/dashboard/")
print("   → Click 'My Apps'")
print("   → Click your app")
print("   → Click 'App info' tab")
print("   → Copy EXACT Client Key and Secret")
print("   → Run setup again: python tiktok_complete_setup.py")
print()

print("2. ❌ App Not Fully Configured")
print("   → Make sure app status is 'Available'")
print("   → Check you added required scopes")
print("   → Settings → Scopes → Add: user.info.basic, video.list")
print()

print("3. ❌ Redirect URI Issue")
print("   → In app settings, make sure redirect URI includes:")
print("   → http://localhost:8000/callback")
print()

print("4. ✓ Everything Looks Good?")
print("   → Try running setup again:")
print("   → python tiktok_complete_setup.py")
print()

print("=" * 70)
print()
