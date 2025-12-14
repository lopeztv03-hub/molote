#!/usr/bin/env python3
"""
AUTO-GENERATE PHASE 2 SETUP
Fully automated - no manual steps!
"""

import os
from pathlib import Path
from dotenv import set_key, load_dotenv

load_dotenv()

print("=" * 75)
print("⚙️  AUTO-GENERATING PHASE 2 SETUP")
print("=" * 75)
print()

# Check current status
print("Checking current configuration...")
print()

client_key = os.getenv("TIKTOK_CLIENT_KEY")
client_secret = os.getenv("TIKTOK_CLIENT_SECRET")
access_token = os.getenv("TIKTOK_ACCESS_TOKEN")

print("Current Status:")
print(f"  Client Key: {'✅ Set' if client_key else '❌ Missing'}")
print(f"  Client Secret: {'✅ Set' if client_secret else '❌ Missing'}")
print(f"  Access Token: {'✅ Set' if access_token else '❌ Missing'}")
print()

# Option 1: If credentials exist but no token
if client_key and client_secret and not access_token:
    print("=" * 75)
    print("✅ CREDENTIALS FOUND - READY FOR OAUTH!")
    print("=" * 75)
    print()
    print("We found your Client Key & Secret.")
    print("Now we need to get your Access Token via OAuth.")
    print()
    
    print("Starting OAuth authentication...")
    print()
    
    try:
        from src.tiktok_api import TikTokAPI
        
        api = TikTokAPI(client_key, client_secret)
        redirect_uri = "http://localhost:8000/callback"
        oauth_url = api.get_oauth_url(redirect_uri)
        
        print("OAuth URL generated:")
        print(f"  {oauth_url}")
        print()
        
        import webbrowser
        try:
            webbrowser.open(oauth_url)
            print("✓ Browser opened for authorization")
        except:
            print("⚠️  Copy URL above and paste in browser")
        
        print()
        code = input("Paste authorization code from browser: ").strip()
        
        if not code:
            print("❌ No code provided")
            exit(1)
        
        print()
        print("Exchanging code for access token...")
        
        if api.exchange_code_for_token(code, redirect_uri):
            env_file = Path(".env")
            set_key(env_file, "TIKTOK_ACCESS_TOKEN", api.access_token)
            if api.refresh_token:
                set_key(env_file, "TIKTOK_REFRESH_TOKEN", api.refresh_token)
            
            print()
            print("=" * 75)
            print("✅ PHASE 2 COMPLETE!")
            print("=" * 75)
            print()
            print("Your bot is now fully configured for real TikTok API!")
            print()
            print("Access Token saved to .env file")
            print()
            print("Run your bot:")
            print("  python full_auto_bot.py")
            print()
        else:
            print("❌ OAuth failed")
            
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\nTry running: python tiktok_oauth_flow.py")

# Option 2: If nothing is configured
else:
    print("=" * 75)
    print("⚠️  CREDENTIALS NOT FOUND")
    print("=" * 75)
    print()
    print("To set up Phase 2, you need:")
    print()
    print("1. TikTok Client Key")
    print("   → Get from: https://developers.tiktok.com/console/app/")
    print("   → Under: App info tab")
    print()
    print("2. TikTok Client Secret")
    print("   → Get from: https://developers.tiktok.com/console/app/")
    print("   → Under: App info tab")
    print()
    print("3. (Optional) TikTok Access Token")
    print("   → Will be auto-generated via OAuth")
    print()
    
    print("Do you have your credentials ready?")
    print()
    
    ready = input("Enter 'yes' if you have Client Key + Secret: ").strip().lower()
    
    if ready == "yes":
        print()
        print("Enter your credentials:")
        print()
        
        client_key = input("Paste Client Key: ").strip()
        client_secret = input("Paste Client Secret: ").strip()
        
        if not client_key or not client_secret:
            print("❌ Missing credentials")
            exit(1)
        
        env_file = Path(".env")
        set_key(env_file, "TIKTOK_CLIENT_KEY", client_key)
        set_key(env_file, "TIKTOK_CLIENT_SECRET", client_secret)
        
        print()
        print("✅ Credentials saved!")
        print()
        print("Now getting access token via OAuth...")
        print()
        
        try:
            from src.tiktok_api import TikTokAPI
            
            api = TikTokAPI(client_key, client_secret)
            redirect_uri = "http://localhost:8000/callback"
            oauth_url = api.get_oauth_url(redirect_uri)
            
            print("Authorization URL:")
            print(f"  {oauth_url}")
            print()
            
            import webbrowser
            try:
                webbrowser.open(oauth_url)
                print("✓ Browser opened")
            except:
                print("⚠️  Copy URL and paste in browser")
            
            print()
            code = input("Paste authorization code: ").strip()
            
            if api.exchange_code_for_token(code, redirect_uri):
                set_key(env_file, "TIKTOK_ACCESS_TOKEN", api.access_token)
                if api.refresh_token:
                    set_key(env_file, "TIKTOK_REFRESH_TOKEN", api.refresh_token)
                
                print()
                print("=" * 75)
                print("✅ PHASE 2 AUTO-GENERATION COMPLETE!")
                print("=" * 75)
                print()
                print("Your bot is configured and ready!")
                print()
                print("Next:")
                print("  python full_auto_bot.py")
                print()
                
        except Exception as e:
            print(f"Error: {e}")
    else:
        print()
        print("Get your credentials first:")
        print("  1. Go to: https://developers.tiktok.com/console/app/")
        print("  2. Click your app")
        print("  3. Copy Client Key + Client Secret")
        print("  4. Run this script again")
        print()

print()
