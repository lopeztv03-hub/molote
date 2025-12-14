#!/usr/bin/env python3
"""
FIX: "Unrecognized App Type" Error
This guide fixes the app type configuration issue
"""

print("""
╔════════════════════════════════════════════════════════════════╗
║       ⚠️  FIX: UNRECOGNIZED APP TYPE ERROR                     ║
╚════════════════════════════════════════════════════════════════╝

WHAT'S WRONG:
Your app doesn't have the correct type set in TikTok Dashboard.

FIX:
Follow these steps to set the app type:

════════════════════════════════════════════════════════════════════

STEP 1: Go to TikTok Developer Console
─────────────────────────────────────

Open: https://developers.tiktok.com/console/app/

Sign in if needed

════════════════════════════════════════════════════════════════════

STEP 2: Click Your App
──────────────────────

You should see your app in the list

┌──────────────────────────────┐
│ My App (or your app name)    │
└──────────────────────────────┘

Click on it

════════════════════════════════════════════════════════════════════

STEP 3: Look for "Application type" or "App Type"
──────────────────────────────────────────────────

On the app details page, look for a section like:

┌────────────────────────────────────┐
│ Application Type:                  │
│ ⭕ Web Application (select this!)  │
│ ⭕ Desktop Application             │
│ ⭕ Server Application              │
└────────────────────────────────────┘

════════════════════════════════════════════════════════════════════

STEP 4: SELECT "Web Application"
───────────────────────────────────

Click the radio button for "Web Application"

This is the correct type for your TikTok bot

════════════════════════════════════════════════════════════════════

STEP 5: Fill in Required Fields
────────────────────────────────

You might see additional fields:

📝 Application Name: 
   → TikTok Bot (or any name)

📝 Application Description:
   → "Automation bot for posting hearts"

📝 Website URL:
   → http://localhost:8000 (for local testing)

📝 Redirect URLs:
   → http://localhost:8000/callback

════════════════════════════════════════════════════════════════════

STEP 6: ADD SCOPES
──────────────────

Look for "Scopes" or "Permissions" section

Check these boxes:

✅ user.info.basic
✅ video.list

════════════════════════════════════════════════════════════════════

STEP 7: SAVE / SUBMIT
─────────────────────

Look for button:

[Save] or [Submit] or [Update]

Click it (usually blue button)

════════════════════════════════════════════════════════════════════

STEP 8: WAIT FOR APPROVAL
─────────────────────────

TikTok might:
✅ Approve instantly (most likely)
⏳ Put in pending (wait for email)
❌ Reject (check email for reason)

If pending, check your email for updates

════════════════════════════════════════════════════════════════════

STEP 9: GET NEW CREDENTIALS
────────────────────────────

Once approved:

1. Go back to app settings
2. Look for "Client Key" and "Client Secret"
3. Copy them (these might be NEW ones)
4. Update your .env file with NEW credentials:
   
   python tiktok_setup.py
   
   (Paste the NEW Client Key)
   (Paste the NEW Client Secret)

════════════════════════════════════════════════════════════════════

STEP 10: RUN SETUP AGAIN
────────────────────────

Once everything is configured:

python tiktok_complete_setup.py

This should now work! ✅

════════════════════════════════════════════════════════════════════

COMMON ISSUES
─────────────

❌ Can't find "Application type" dropdown
   → You might be in wrong tab
   → Try: Overview, Settings, or App info
   → Refresh the page

❌ "Web Application" option grayed out
   → App might already be submitted
   → Try changing to different type first, then back

❌ Status shows "Rejected"
   → Check email for rejection reason
   → Common reasons: missing fields, invalid URLs
   → Fix and resubmit

════════════════════════════════════════════════════════════════════

READY?
──────

1. Go to: https://developers.tiktok.com/console/app/
2. Click your app
3. Set Application Type: Web Application
4. Add Website URL: http://localhost:8000
5. Add Redirect URL: http://localhost:8000/callback
6. Check Scopes: user.info.basic, video.list
7. Save/Submit
8. Wait for approval email
9. Get NEW Client Key + Secret
10. Run: python tiktok_setup.py
11. Run: python tiktok_complete_setup.py

════════════════════════════════════════════════════════════════════
""")

input("\n\n📌 Fix the app type, then run: python tiktok_complete_setup.py\n\nPress Enter when done...")
