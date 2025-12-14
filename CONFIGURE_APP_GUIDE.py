#!/usr/bin/env python3
"""
STEP-BY-STEP: Configure Your TikTok App
This guide shows exactly what to click and where
"""

print("""
╔════════════════════════════════════════════════════════════════╗
║       🎬 CONFIGURE YOUR TIKTOK APP (STEP BY STEP)              ║
╚════════════════════════════════════════════════════════════════╝

WHAT WE'RE DOING:
We need to add Scopes and Redirect URI to your app so OAuth works.

TIME: 2-3 minutes

════════════════════════════════════════════════════════════════════

PART 1: ADD SCOPES
──────────────────

Follow these EXACT steps:

1️⃣  Open: https://developers.tiktok.com/console/app/

2️⃣  You'll see your app listed
    Click on it

    ┌──────────────────────┐
    │ My App               │
    │ [created recently]   │
    └──────────────────────┘
    👆 CLICK HERE

3️⃣  You're now in app details
    Look for tabs at top:
    
    ┌─────────────────────────────────────┐
    │ Overview | Settings | Permissions   │
    │          (or similar tabs)          │
    └─────────────────────────────────────┘

4️⃣  Click "Settings" tab

5️⃣  Look for "Scopes" section
    
    You'll see checkboxes or a list:
    
    ☐ user.info.basic
    ☐ video.list
    ☐ video.publish
    (and others)

6️⃣  CHECK these scopes:
    
    ✅ user.info.basic
    ✅ video.list

    (Leave others unchecked unless needed)

7️⃣  Scroll down and SAVE

    Look for blue button:
    [Save] or [Update] or [Apply]
    👆 CLICK IT

✅ SCOPES ADDED!

════════════════════════════════════════════════════════════════════

PART 2: ADD REDIRECT URI
────────────────────────

1️⃣  Still in "Settings" tab

2️⃣  Look for "Redirect URLs" or "Callback URLs"
    
    You might see:
    
    Redirect URL(s):
    ┌─────────────────────────────┐
    │ [Add URL] or [+ Add]        │
    └─────────────────────────────┘

3️⃣  Click [Add URL] button

4️⃣  Paste this EXACTLY:
    
    http://localhost:8000/callback

    ⚠️  MUST BE EXACT - no typos!

5️⃣  Click Add or Save

✅ REDIRECT URI ADDED!

════════════════════════════════════════════════════════════════════

PART 3: CHECK APP STATUS
────────────────────────

1️⃣  Go back to app overview

2️⃣  Look for "Status" field
    
    It should say:
    ✅ "Available" or "Active"
    
    NOT "Pending" or "Rejected"

3️⃣  If it's not available:
    → You might need to wait
    → Check for approval emails
    → Complete any missing steps TikTok shows

════════════════════════════════════════════════════════════════════

ALL DONE? ✅
────────────

Once you've added Scopes and Redirect URI:

1. Close TikTok Developer Dashboard
2. Come back to your bot folder
3. Run: python tiktok_complete_setup.py
4. Follow the OAuth flow
5. ✅ Bot posts real hearts to TikTok!

════════════════════════════════════════════════════════════════════

STUCK? COMMON ISSUES
────────────────────

❌ Can't find Scopes section
   → You might be in wrong tab
   → Try "Settings" or "Permissions" tab
   → Refresh page

❌ Redirect URI field grayed out
   → App might not be approved yet
   → Wait for approval email
   → Or contact TikTok support

❌ Can't save changes
   → Try logging out and back in
   → Clear browser cache
   → Try different browser

════════════════════════════════════════════════════════════════════

READY?
──────

1. Go to: https://developers.tiktok.com/console/app/
2. Click your app
3. Click Settings
4. Add Scopes: user.info.basic, video.list
5. Add Redirect: http://localhost:8000/callback
6. Save
7. Come back here and run: python tiktok_complete_setup.py

════════════════════════════════════════════════════════════════════
""")

input("\n\n📌 Go configure your app, then come back and run tiktok_complete_setup.py\n\nPress Enter when done...")
