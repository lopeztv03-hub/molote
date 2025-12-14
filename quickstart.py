#!/usr/bin/env python3
"""
QUICKSTART - Just Run This!
Automatically runs the bot with no input needed
"""

import sys
import os

# Make sure we're in the right directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print("=" * 70)
print("🎬 TIKTOK BOT - QUICKSTART")
print("=" * 70)
print()

# Import and run directly
try:
    from src.video_watcher_agent import VideoWatcherAgent
    from src.mock_tiktok_api import MockTikTokAPI
    
    print("Initializing bot...")
    print()
    
    # Setup - Using REAL TikTok API
    from src.tiktok_api import TikTokAPI
    import os
    from dotenv import load_dotenv
    
    load_dotenv()
    
    tiktok_api = TikTokAPI(
        client_key=os.getenv("TIKTOK_CLIENT_KEY"),
        client_secret=os.getenv("TIKTOK_CLIENT_SECRET")
    )
    
    agent = VideoWatcherAgent(use_real_api=True)
    agent.configure_tiktok_api(
        os.getenv("TIKTOK_CLIENT_KEY"),
        os.getenv("TIKTOK_CLIENT_SECRET")
    )
    
    # Add video
    url = "https://www.tiktok.com/@cirumtv/photo/7582521253030907150?q=cirumtv&t=1765698401325"
    agent.add_video(url, "Cirum TikTok")
    
    print("✓ Video added")
    print()
    
    # Post hearts - REAL API
    print("Getting OAuth token...")
    oauth_url = tiktok_api.get_oauth_url(
        redirect_uri="http://localhost:8000/callback",
        scope=["user.info.basic", "video.list"]
    )
    print(f"✓ OAuth URL generated")
    print()
    
    print("Posting 50 REAL hearts to your TikTok video...")
    success, results = tiktok_api.heart_video_multi("7582521253030907150", 50)
    agent.heart_video_multi_with_api("1", "7582521253030907150", success)
    
    print(f"✓ Posted {success} hearts")
    print()
    
    # Show results
    print("=" * 70)
    print("✅ RESULTS")
    print("=" * 70)
    print()
    
    video = agent.watched_videos["1"]
    hearts = agent.get_bot_heart_count("1")
    
    print(f"Video: {video['title']}")
    print(f"Platform: {video['platform']}")
    print(f"❤️  Hearts: {hearts}")
    print()
    print("Status: ✅ SUCCESS")
    print()
    print("=" * 70)
    
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
