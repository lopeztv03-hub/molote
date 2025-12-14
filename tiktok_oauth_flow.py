#!/usr/bin/env python3
"""
TikTok OAuth Flow Helper
Guides users through the OAuth authentication process
"""

import webbrowser
from src.tiktok_api import TikTokAPI
from dotenv import set_key
from pathlib import Path


def oauth_flow():
    """Interactive OAuth authentication flow"""
    print("=" * 70)
    print("🔐 TikTok OAuth Authentication")
    print("=" * 70)
    print()
    
    # Initialize API
    api = TikTokAPI()
    
    if not api.client_key or not api.client_secret:
        print("✗ TikTok credentials not configured")
        print("  Run: python tiktok_setup.py")
        return False
    
    print("Step 1: Opening TikTok authorization page...")
    print()
    
    # Generate OAuth URL
    redirect_uri = "http://localhost:8000/callback"
    oauth_url = api.get_oauth_url(redirect_uri)
    
    print(f"Authorization URL:")
    print(f"  {oauth_url}")
    print()
    
    # Try to open in browser
    try:
        webbrowser.open(oauth_url)
        print("✓ Browser opened (if not, copy the URL above)")
    except:
        print("⚠️  Couldn't open browser automatically")
        print("   Please copy and paste the URL above into your browser")
    
    print()
    print("Step 2: Authorize the bot")
    print("  1. Log in with your TikTok account")
    print("  2. Click 'Authorize'")
    print("  3. You'll be redirected to a callback URL")
    print()
    
    # Get authorization code
    print("Step 3: Enter the authorization code")
    code = input("Enter the code from the callback URL: ").strip()
    
    if not code:
        print("✗ No code provided")
        return False
    
    print()
    print("Step 4: Exchanging code for access token...")
    
    # Exchange code for token
    success = api.exchange_code_for_token(code, redirect_uri)
    
    if not success:
        print("✗ Failed to get access token")
        return False
    
    # Save access token
    env_file = Path(".env")
    if not env_file.exists():
        env_file = Path(__file__).parent / ".env"
    
    try:
        set_key(env_file, "TIKTOK_ACCESS_TOKEN", api.access_token)
        if api.refresh_token:
            set_key(env_file, "TIKTOK_REFRESH_TOKEN", api.refresh_token)
        
        print()
        print("=" * 70)
        print("✅ Authentication Successful!")
        print("=" * 70)
        print()
        print(f"Access Token: {api.access_token[:30]}...")
        print(f"Saved to: {env_file.absolute()}")
        print()
        print("Your bot can now post real hearts to TikTok!")
        print()
        print("Next steps:")
        print("  1. Run: python video_watcher.py")
        print("  2. Add a TikTok video URL")
        print("  3. Use command 13 to heart the video")
        print()
        
        return True
        
    except Exception as e:
        print(f"✗ Failed to save token: {e}")
        return False


if __name__ == "__main__":
    oauth_flow()
