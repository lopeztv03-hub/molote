#!/usr/bin/env python3
"""
Setup Verification Script
Checks if your TikTok app is configured correctly
"""

import os
from dotenv import load_dotenv

load_dotenv()

print("=" * 70)
print("🔍 TIKTOK API SETUP VERIFICATION")
print("=" * 70)
print()

# Check credentials
client_key = os.getenv("TIKTOK_CLIENT_KEY")
client_secret = os.getenv("TIKTOK_CLIENT_SECRET")

print("✓ Checking credentials...")
print()

if not client_key or client_key == "awaicogeixafljoq":
    print("⚠️  Using default test credentials")
    print("   These may not work with your TikTok app")
    print()
    print("   To fix: Get your credentials from TikTok Developer Dashboard:")
    print("   1. Go to https://developer.tiktok.com/")
    print("   2. Open your app")
    print("   3. Copy Client Key and Client Secret")
    print("   4. Update .env file:")
    print("      TIKTOK_CLIENT_KEY=your_key")
    print("      TIKTOK_CLIENT_SECRET=your_secret")
    print()
else:
    print(f"✓ Client Key: {client_key[:20]}...")
    print(f"✓ Client Secret: {client_secret[:20]}...")
    print()

# Try to initialize API
print("✓ Testing API initialization...")
print()

try:
    from src.tiktok_api import TikTokAPI
    
    api = TikTokAPI(
        client_key=client_key,
        client_secret=client_secret
    )
    
    print("✓ TikTok API initialized successfully")
    print()
    
    # Try to generate OAuth URL
    print("✓ Testing OAuth URL generation...")
    oauth_url = api.get_oauth_url(
        redirect_uri="http://localhost:8000/callback",
        scope=["user.info.basic", "video.list"]
    )
    print("✓ OAuth URL generated successfully")
    print()
    
    print("=" * 70)
    print("✅ SETUP IS READY!")
    print("=" * 70)
    print()
    print("You can now run:")
    print("  python full_auto_bot.py")
    print("  OR")
    print("  double-click START_BOT.bat")
    print()
    
except Exception as e:
    print(f"❌ Error: {e}")
    print()
    print("=" * 70)
    print("⚠️  SETUP NEEDED")
    print("=" * 70)
    print()
    print("Follow these steps:")
    print()
    print("1. Read: SETUP_REAL_API.md")
    print()
    print("2. Go to: https://developer.tiktok.com/")
    print()
    print("3. Create or select your app")
    print()
    print("4. Configure:")
    print("   - App Type: Web Application")
    print("   - Scopes: user.info.basic, video.list")
    print("   - Redirect: http://localhost:8000/callback")
    print()
    print("5. Copy credentials from Dashboard")
    print()
    print("6. Update .env file with your credentials")
    print()
    print("7. Run this script again")
    print()
