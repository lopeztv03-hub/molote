# 🎬 REAL TIKTOK API SETUP - QUICK START

## What Changed?

Your bot is now configured to post **REAL hearts** to TikTok! 🎉

Previously: Mock API (simulated hearts locally)
Now: Real TikTok API (actual hearts on your video)

## 3 Ways to Setup

### Option 1: FASTEST - Interactive Setup Guide (Recommended)
```bash
python SETUP_GUIDE.py
```
This will walk you through everything step-by-step.

### Option 2: Manual Setup
1. Read [SETUP_REAL_API.md](SETUP_REAL_API.md)
2. Go to https://developer.tiktok.com/
3. Configure your app
4. Copy credentials
5. Update .env file

### Option 3: Verify Existing Setup
```bash
python VERIFY_SETUP.py
```
Checks if your app is configured correctly.

## Quick Checklist

Before running the bot, make sure:

- [ ] You have a TikTok account (any account works)
- [ ] You've created an app at https://developer.tiktok.com/
- [ ] App Type is set to "Web Application"
- [ ] You've added OAuth scopes:
  - user.info.basic
  - video.list
  - user.liking (for hearts)
- [ ] You've added redirect URI: `http://localhost:8000/callback`
- [ ] You've copied Client Key and Client Secret to .env file

## Files Updated

### New Files:
- `SETUP_GUIDE.py` - Interactive setup wizard
- `VERIFY_SETUP.py` - Check if setup is complete
- `SETUP_REAL_API.md` - Detailed setup instructions
- `START_BOT.bat` - Simple batch launcher for Windows
- `quickstart.py` - Simplified bot launcher

### Modified Files:
- `full_auto_bot.py` - Now uses Real TikTok API
- `.env` - Contains your credentials

## Run the Bot

### Windows Users:
Double-click: `START_BOT.bat`

### Command Line:
```bash
python full_auto_bot.py
```

### Using Setup Guide First:
```bash
python SETUP_GUIDE.py
```

## What Happens When You Run It?

1. Bot connects to TikTok API with your credentials
2. Bot generates an OAuth authorization URL
3. Bot asks for permission to like videos
4. Bot posts 50 REAL hearts to your Cirum TikTok video
5. Results are displayed (# of hearts posted)

## Important Notes

- **First Run**: You may need to authorize the app to post hearts
- **Rate Limits**: TikTok has rate limits (you can post ~50 hearts quickly)
- **Account**: The bot uses YOUR account to post hearts
- **Error 404**: If you get a 404 error, your app isn't configured as "Web Application" in the Dashboard

## Troubleshooting

### "Error: 404"
- Go to TikTok Developer Dashboard
- Make sure App Type is "Web Application"
- Add redirect URI: http://localhost:8000/callback
- Save changes and try again

### "Error: Invalid credentials"
- Check that Client Key and Secret are correct
- Go to dashboard and copy them again
- Update .env file

### "Error: OAuth failed"
- Make sure you're logged into TikTok
- Try logging out and back in
- Or try with a different TikTok account

## Questions?

Read [SETUP_REAL_API.md](SETUP_REAL_API.md) for detailed instructions.

---

**Ready to post REAL hearts?** Run one of these:

```bash
python SETUP_GUIDE.py         # Interactive setup
python full_auto_bot.py       # Run the bot
python VERIFY_SETUP.py        # Check setup
```

Or double-click: `START_BOT.bat`

🚀 Let's go!
