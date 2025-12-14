"""
HOW TO GET CLIENT KEY FROM TIKTOK DEVELOPERS
=============================================

Follow these steps EXACTLY to find your Client Key
"""

print("""
╔═══════════════════════════════════════════════════════════════╗
║         📋 HOW TO GET YOUR TIKTOK CLIENT KEY                  ║
╚═══════════════════════════════════════════════════════════════╝

STEP 1: Go to TikTok Developers
────────────────────────────────

Open this URL in your browser:
   👉 https://developers.tiktok.com/

   OR

   1. Google: "TikTok developers"
   2. Click: https://www.tiktok.com/developers/

═══════════════════════════════════════════════════════════════════

STEP 2: Sign In
────────────────

Click "Sign In" in the top right

Use your TikTok account:
   - Email address
   - Password
   - Complete verification if asked

═══════════════════════════════════════════════════════════════════

STEP 3: Go To Your Apps
───────────────────────

On the left sidebar, click: "My Apps"

You should see your app listed:
   (The app you just created)

═══════════════════════════════════════════════════════════════════

STEP 4: Open App Settings
──────────────────────────

Click on your app name

You'll see several tabs at the top:
   • App info (or Overview)  ← CLICK THIS
   • Settings
   • Development
   • etc.

═══════════════════════════════════════════════════════════════════

STEP 5: Find Your Credentials
──────────────────────────────

On the "App info" tab, scroll down.

You'll see a box with:

┌─────────────────────────────────────┐
│  CLIENT KEY (or API KEY)            │
│                                     │
│  Example:                           │
│  abc123def456ghi789jkl012mno345     │
│                                     │
│  [Copy button] ← CLICK TO COPY      │
└─────────────────────────────────────┘

And below it:

┌─────────────────────────────────────┐
│  CLIENT SECRET (or API SECRET)      │
│                                     │
│  Example:                           │
│  xyz789abc456def123ghi012jkl345     │
│                                     │
│  [Copy button] ← CLICK TO COPY      │
└─────────────────────────────────────┘

═══════════════════════════════════════════════════════════════════

STEP 6: Copy Your Credentials
──────────────────────────────

1. Click "Copy" next to CLIENT KEY
   ✓ You now have Client Key in clipboard

2. Paste it somewhere safe temporarily
   (like a text file)

3. Click "Copy" next to CLIENT SECRET
   ✓ You now have Client Secret in clipboard

4. Save that too

═══════════════════════════════════════════════════════════════════

STEP 7: IMPORTANT - Keep Them Secret!
─────────────────────────────────────

⚠️  DO NOT:
   ❌ Share with anyone
   ❌ Post on social media
   ❌ Commit to GitHub
   ❌ Put in public code

✅ DO:
   ✓ Keep in .env file (secure)
   ✓ Only on your computer
   ✓ Treat like a password

═══════════════════════════════════════════════════════════════════

NOW WHAT?
─────────

Once you have both credentials:

1. Open PowerShell in bot folder
2. Run: python tiktok_complete_setup.py
3. Paste Client Key when asked
4. Paste Client Secret when asked
5. Follow OAuth instructions
6. Done! Your bot posts real hearts! ✅

═══════════════════════════════════════════════════════════════════

STILL STUCK?
────────────

Common issues:

❓ Can't find "My Apps"
   → Make sure you're logged in
   → Refresh page
   → Try https://developers.tiktok.com/dashboard/

❓ No Client Key visible
   → Click "App info" tab
   → Scroll down
   → It should be there

❓ Getting an error
   → Make sure app is created
   → Wait a minute, refresh, try again

═══════════════════════════════════════════════════════════════════

READY TO GET YOUR KEY?
──────────────────────

Go to: https://developers.tiktok.com/
Sign in → My Apps → Click app → App info tab → Copy Client Key

Then run: python tiktok_complete_setup.py

═══════════════════════════════════════════════════════════════════
""")

input("\n\n📌 Go get your Client Key, then run tiktok_complete_setup.py\n")
