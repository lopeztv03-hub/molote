#!/usr/bin/env python3
"""
PHASE 2: UPGRADE TO REAL TIKTOK API
Complete setup guide for real credentials
"""

print("""
╔════════════════════════════════════════════════════════════════╗
║          🚀 PHASE 2: REAL TIKTOK API UPGRADE                   ║
╚════════════════════════════════════════════════════════════════╝

You're ready to upgrade to REAL TikTok API!
Your bot will post ACTUAL hearts to TikTok.

═══════════════════════════════════════════════════════════════════

QUICK CHECKLIST (3 Steps, 10 minutes):
──────────────────────────────────────

✓ STEP 1: Get TikTok API Credentials
   └─ Go to: https://developers.tiktok.com/
   └─ Create app (if not done)
   └─ Set App Type: "Web Application"
   └─ Copy Client Key + Client Secret

✓ STEP 2: Configure Your Bot
   └─ Run: python tiktok_setup.py
   └─ Paste Client Key
   └─ Paste Client Secret

✓ STEP 3: Authenticate with OAuth
   └─ Run: python tiktok_oauth_flow.py
   └─ Authorize in browser
   └─ Done! ✅

═══════════════════════════════════════════════════════════════════

BEFORE YOU START:
─────────────────

Make sure you've completed these in TikTok Dashboard:

✅ App Created
✅ App Type: Web Application
✅ Scopes Added: user.info.basic, video.list
✅ Redirect URL: http://localhost:8000/callback

If not, do that first at: https://developers.tiktok.com/console/app/

═══════════════════════════════════════════════════════════════════

READY? LET'S START!
──────────────────

In your PowerShell terminal, run these in order:

STEP 1: Setup Credentials
────────────────────────

Command:
  python tiktok_setup.py

What happens:
  • Asks for Client Key (paste from TikTok Dashboard)
  • Asks for Client Secret (paste from TikTok Dashboard)
  • Saves to .env file
  • Takes ~1 minute

═══════════════════════════════════════════════════════════════════

STEP 2: OAuth Authentication
──────────────────────────────

Command:
  python tiktok_oauth_flow.py

What happens:
  • Opens TikTok authorization page in browser
  • You authorize the bot
  • Redirects with authorization code
  • Pastes code back into bot
  • Gets access token automatically
  • Saves token to .env file
  • Takes ~2 minutes

═══════════════════════════════════════════════════════════════════

STEP 3: Test & Use
──────────────────

Command:
  python full_auto_bot.py

Now your bot will:
  ✅ Post REAL hearts to TikTok
  ✅ Track engagement
  ✅ Work with real API

═══════════════════════════════════════════════════════════════════

TROUBLESHOOTING:
────────────────

❌ "App Type Error"
   → Make sure app type is "Web Application"
   → Check: https://developers.tiktok.com/console/app/

❌ "OAuth Failed"
   → Make sure you authorized the app
   → Check callback URL: http://localhost:8000/callback

❌ "Invalid Credentials"
   → Copy Client Key/Secret exactly (no spaces)
   → Make sure they're from App info tab

═══════════════════════════════════════════════════════════════════

YOUR BOT AFTER PHASE 2:
──────────────────────

✅ Posts REAL hearts to TikTok
✅ Tracks all engagement
✅ Handles rate limiting
✅ Fully automated
✅ Ready for production

═══════════════════════════════════════════════════════════════════

LET'S DO THIS! 🚀
─────────────────

Step 1:
  python tiktok_setup.py

Step 2:
  python tiktok_oauth_flow.py

Step 3:
  python full_auto_bot.py

═══════════════════════════════════════════════════════════════════
""")

input("\n\n📌 Ready to start Phase 2? Press Enter...\n")

# Ask which step to start with
print("\nWhat would you like to do?")
print("  1. Run Setup (python tiktok_setup.py)")
print("  2. Run OAuth (python tiktok_oauth_flow.py)")
print("  3. Test Bot (python full_auto_bot.py)")
print("  4. Exit")

choice = input("\nEnter choice (1-4): ").strip()

if choice == "1":
    print("\nRunning: python tiktok_setup.py\n")
    import subprocess
    subprocess.run(["python", "tiktok_setup.py"])

elif choice == "2":
    print("\nRunning: python tiktok_oauth_flow.py\n")
    import subprocess
    subprocess.run(["python", "tiktok_oauth_flow.py"])

elif choice == "3":
    print("\nRunning: python full_auto_bot.py\n")
    import subprocess
    subprocess.run(["python", "full_auto_bot.py"])

else:
    print("\nExiting. Run 'python phase2_setup.py' when ready!\n")
