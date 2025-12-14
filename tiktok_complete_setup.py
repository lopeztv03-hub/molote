#!/usr/bin/env python3
"""
Interactive TikTok API Credential Extractor & Setup Helper
Guides you through getting credentials from TikTok Developer Dashboard
"""

import time
import webbrowser

def show_credentials_guide():
    """Show visual guide for finding credentials"""
    print("\n" + "=" * 75)
    print("🔐 FINDING YOUR TIKTOK API CREDENTIALS")
    print("=" * 75)
    print()
    
    print("STEP 1: Go to TikTok Developer Dashboard")
    print("─" * 75)
    print("  1. Open: https://developers.tiktok.com/")
    print("  2. Sign in (if not already)")
    print("  3. Click 'My Apps' in the left sidebar")
    print()
    
    input("📌 Press Enter when you're in 'My Apps'...")
    
    print()
    print("STEP 2: Select Your App")
    print("─" * 75)
    print("  1. Click on the app you just created")
    print("  2. Go to 'Settings' or 'App info' tab")
    print()
    
    input("📌 Press Enter when you see the app details...")
    
    print()
    print("STEP 3: Find Your Credentials")
    print("─" * 75)
    print("  You should see:")
    print()
    print("  ┌─────────────────────────────────────────┐")
    print("  │ CLIENT KEY (also called API Key)         │")
    print("  │ Example: abc123def456ghi789...           │")
    print("  └─────────────────────────────────────────┘")
    print()
    print("  ┌─────────────────────────────────────────┐")
    print("  │ CLIENT SECRET (also called API Secret)   │")
    print("  │ Example: xyz789abc456def123...           │")
    print("  └─────────────────────────────────────────┘")
    print()
    
    print("✅ Have them ready? Let's configure the bot...")
    time.sleep(2)

def run_setup_interactive():
    """Run tiktok_setup.py interactively"""
    print()
    print("=" * 75)
    print("⚙️  CONFIGURING YOUR BOT WITH CREDENTIALS")
    print("=" * 75)
    print()
    
    print("Now we'll save your credentials to the bot.")
    print()
    
    input("Press Enter to start the setup script...")
    
    # Import and run setup
    from dotenv import set_key
    from pathlib import Path
    import os
    
    # Get credentials
    print()
    print("Step 1: Enter your TikTok Client Key")
    print("-" * 75)
    while True:
        client_key = input("Paste Client Key here: ").strip()
        if client_key and len(client_key) > 10:
            print(f"  ✓ Saved: {client_key[:20]}...")
            break
        print("  ✗ Invalid. Please paste the full Client Key")
    
    print()
    print("Step 2: Enter your TikTok Client Secret")
    print("-" * 75)
    while True:
        client_secret = input("Paste Client Secret here: ").strip()
        if client_secret and len(client_secret) > 10:
            print(f"  ✓ Saved: {client_secret[:20]}...")
            break
        print("  ✗ Invalid. Please paste the full Client Secret")
    
    # Save to .env
    env_file = Path(".env")
    if not env_file.exists():
        env_file = Path(__file__).parent / ".env"
    
    print()
    print("Saving to .env file...")
    
    try:
        set_key(env_file, "TIKTOK_CLIENT_KEY", client_key)
        set_key(env_file, "TIKTOK_CLIENT_SECRET", client_secret)
        print(f"  ✓ Credentials saved!")
        print(f"  📁 Location: {env_file.absolute()}")
    except Exception as e:
        print(f"  ✗ Error: {e}")
        return False
    
    return True

def run_oauth_flow():
    """Run OAuth authentication"""
    print()
    print("=" * 75)
    print("🔓 AUTHENTICATING WITH TIKTOK (OAuth)")
    print("=" * 75)
    print()
    
    print("This will:")
    print("  1. Open TikTok authorization page")
    print("  2. Ask you to authorize the bot")
    print("  3. Get your access token automatically")
    print()
    
    input("Press Enter to start OAuth flow...")
    
    print()
    print("Opening TikTok authorization page in browser...")
    print()
    
    from src.tiktok_api import TikTokAPI
    
    api = TikTokAPI()
    
    if not api.client_key or not api.client_secret:
        print("✗ Credentials not found. Please run setup first.")
        return False
    
    # Generate OAuth URL
    redirect_uri = "http://localhost:8000/callback"
    oauth_url = api.get_oauth_url(redirect_uri)
    
    print("OAuth URL:")
    print(f"  {oauth_url}")
    print()
    
    # Try to open browser
    try:
        webbrowser.open(oauth_url)
        print("✓ Browser opened!")
    except:
        print("⚠️  Browser didn't open. Copy the URL above and paste into browser.")
    
    print()
    print("─" * 75)
    print("WHAT TO DO IN YOUR BROWSER:")
    print("─" * 75)
    print("  1. Log in with your TikTok account")
    print("  2. Click 'Authorize' to give the bot permission")
    print("  3. You'll see a page with a code")
    print()
    
    # Get authorization code
    code = input("Paste the authorization code here: ").strip()
    
    if not code:
        print("✗ No code provided")
        return False
    
    print()
    print("Getting access token...")
    
    if api.exchange_code_for_token(code, redirect_uri):
        print()
        print("=" * 75)
        print("✅ SUCCESS! YOUR BOT IS AUTHENTICATED!")
        print("=" * 75)
        print()
        print(f"  Access Token: {api.access_token[:30]}...")
        print(f"  Status: READY TO POST HEARTS!")
        print()
        return True
    else:
        print("✗ OAuth failed. Try again.")
        return False

def show_next_steps():
    """Show what to do next"""
    print()
    print("=" * 75)
    print("🎉 SETUP COMPLETE! NEXT STEPS:")
    print("=" * 75)
    print()
    
    print("Your bot can now post REAL hearts to TikTok!")
    print()
    
    print("OPTION 1: Test in interactive mode")
    print("─" * 75)
    print("  Command: python video_watcher.py")
    print("  1. Command: 1 (add)")
    print("  2. URL: https://www.tiktok.com/@cirumtv/photo/7582521253030907150")
    print("  3. Title: Cirum TikTok")
    print("  4. Command: 13 (hearts)")
    print("  5. Video ID: 1")
    print("  6. Bots: 50")
    print()
    print("  Your video WILL get 50 real hearts! ❤️")
    print()
    
    print("OPTION 2: Run demo with real API")
    print("─" * 75)
    print("  Command: python add_video.py")
    print("  (Posts real hearts to your video)")
    print()
    
    print("─" * 75)
    print("Questions? Check README.md for TikTok API docs")
    print("=" * 75)
    print()


if __name__ == "__main__":
    import sys
    
    try:
        # Show credentials guide
        show_credentials_guide()
        
        # Setup
        if not run_setup_interactive():
            sys.exit(1)
        
        # OAuth
        if not run_oauth_flow():
            sys.exit(1)
        
        # Next steps
        show_next_steps()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Setup cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n✗ Error: {e}")
        sys.exit(1)
