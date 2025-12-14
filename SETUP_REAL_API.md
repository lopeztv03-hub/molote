# Real TikTok API Setup Guide

## Step 1: Go to TikTok Developer Dashboard
1. Visit: https://developer.tiktok.com/
2. Sign in with your TikTok account (or the one that owns @cirumtv)
3. Click "Create an app"

## Step 2: Configure Your App

**App Details:**
- **App Name:** Cirum Bot (or whatever you want)
- **App Type:** Select **"Web Application"** (IMPORTANT!)
- **Description:** Automation bot for TikTok engagement
- **Category:** Automation

## Step 3: Add OAuth Scopes

Go to **"Scopes"** and enable these:
- ✅ `user.info.basic` - Read user profile
- ✅ `video.list` - List videos
- ✅ `video.publish` - Post content (if available)
- ✅ `user.liking` - Like videos (THIS ONE IS KEY!)

## Step 4: Set Redirect URI

In **"Redirect URIs"** section, add:
```
http://localhost:8000/callback
```

## Step 5: Copy Your Credentials

You should see:
- **Client Key** 
- **Client Secret**

Copy these and verify they match what's in your `.env` file:
```
TIKTOK_CLIENT_KEY=awaicogeixafljoq
TIKTOK_CLIENT_SECRET=JJvYr37B72MIk3BUpLUXNuZ4WMFDD5JW
```

If they don't match, update your `.env` file with the new ones from the Dashboard.

## Step 6: Test OAuth Connection

Once configured, the bot will:
1. Generate an OAuth URL
2. Open it in your browser
3. Ask for permission
4. Get an access token
5. Start posting real hearts

## Common Issues

**Issue: Still getting 404 error**
- Make sure app type is "Web Application" (not "Web" or other)
- Check that scopes are saved properly
- Verify redirect URI is exactly: `http://localhost:8000/callback`

**Issue: OAuth popup doesn't appear**
- Make sure your app is in "Live" status (not "Development")
- Check TikTok dashboard for any validation errors

## After Setup

The bot will automatically:
- Get an OAuth token when you run it
- Use that token to post hearts
- Refresh the token when needed
- Post REAL hearts to your TikTok video!

---

**Questions?** The real API integration is already coded—you just need to configure the app dashboard.
