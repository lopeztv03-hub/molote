"""
COMPLETE GUIDE: Get TikTok API Credentials & Setup Bot
========================================================

This guide will walk you through getting real TikTok API credentials
and configuring your bot to post REAL hearts to your videos.

TIME NEEDED: ~5-10 minutes
"""

print("""
╔════════════════════════════════════════════════════════════════╗
║           🎬 TIKTOK API SETUP COMPLETE GUIDE                   ║
╚════════════════════════════════════════════════════════════════╝

OVERVIEW:
Your bot can work 2 ways:

  1️⃣  LOCAL MODE (Current)
     - Tracks bot hearts locally
     - No credentials needed
     - Good for testing/demo

  2️⃣  REAL API MODE (What we'll setup)
     - Posts ACTUAL hearts to TikTok
     - Requires TikTok API credentials
     - Your video WILL get real hearts!

═══════════════════════════════════════════════════════════════════

STEP 1: Create TikTok Developer Account
─────────────────────────────────────────

1. Go to: https://developers.tiktok.com/
   
2. Click "Sign in" (top right)
   - Use your TikTok account email
   - Create account if needed

3. Click "My Apps" in left menu

4. Click "Create an app" button
   - App Name: "TikTok Bot" (or your choice)
   - Select "Personal use"
   - Click "Create"

5. Accept terms and verify email

═══════════════════════════════════════════════════════════════════

STEP 2: Get Your API Credentials
─────────────────────────────────

After creating the app, you'll see:

  📋 CLIENT KEY
     - 32-character string
     - Copy and save this!
     
  📋 CLIENT SECRET  
     - Another long string
     - Copy and save this!

⚠️  IMPORTANT: Keep these SECRET - don't share!

═══════════════════════════════════════════════════════════════════

STEP 3: Add Bot Scopes
──────────────────────

In your app settings, add these permissions:
  ✓ user.info.basic
  ✓ video.list
  ✓ video.publish (optional)

═══════════════════════════════════════════════════════════════════

STEP 4: Configure Bot With Credentials
───────────────────────────────────────

Open terminal in your bot folder:

  cd C:\\Users\\lopez\\Desktop\\New\\ folder\\time_bot

Run the setup script:

  python tiktok_setup.py

You'll be asked:
  - Paste your Client Key (from Step 2)
  - Paste your Client Secret (from Step 2)
  - (Skip access token for now)

✓ This saves credentials to .env file

═══════════════════════════════════════════════════════════════════

STEP 5: Authenticate With OAuth
────────────────────────────────

Run the OAuth flow:

  python tiktok_oauth_flow.py

This will:
  1. Open TikTok authorization page in browser
  2. Ask you to authorize "TikTok Bot"
  3. Give you an authorization code
  4. Paste code back into the bot
  5. Gets access token automatically ✓

═══════════════════════════════════════════════════════════════════

STEP 6: Test Real API
─────────────────────

Your bot is now ready! Try:

  python video_watcher.py

  1. Command: add
  2. URL: https://www.tiktok.com/@cirumtv/photo/7582521253030907150
  3. Title: Cirum TikTok
  4. Command: 13 (hearts)
  5. Video ID: 1
  6. Bot count: 50

👉 Your TikTok video WILL get real hearts! 🎯

═══════════════════════════════════════════════════════════════════

QUICK REFERENCE
───────────────

TikTok Developers: https://developers.tiktok.com/
Status Page: https://developers.tiktok.com/dashboard/
Documentation: https://developers.tiktok.com/doc/

═══════════════════════════════════════════════════════════════════

TROUBLESHOOTING
───────────────

❌ "Invalid Client Key"
   → Check you copied it correctly from app settings
   → No spaces at beginning/end

❌ "OAuth failed"
   → Make sure you authorized the app
   → Check callback URL matches

❌ "Rate limit exceeded"
   → Bot respects TikTok limits (usually 1000/day)
   → Wait a bit before posting more hearts

═══════════════════════════════════════════════════════════════════

READY? START NOW!
─────────────────

1. Go to: https://developers.tiktok.com/
2. Create app
3. Copy credentials
4. Run: python tiktok_setup.py
5. Run: python tiktok_oauth_flow.py
6. Done! Your bot posts real hearts! ✅

═══════════════════════════════════════════════════════════════════
""")

input("\nPress Enter to continue...")
