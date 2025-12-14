#!/usr/bin/env python3
"""
Quick test of TikTok API integration with your video
(Works locally - requires credentials for real posting)
"""

from src.video_watcher_agent import VideoWatcherAgent

# Your TikTok video
url = "https://www.tiktok.com/@cirumtv/photo/7582521253030907150?q=cirumtv&t=1765698401325"
title = "Cirum TikTok"

print("=" * 70)
print("🎬 TIKTOK API TEST - Cirum Video")
print("=" * 70)
print()

# Create agent
agent = VideoWatcherAgent(use_real_api=False)  # Start without API

# Add your video
agent.add_video(url, title)

print()
print("=" * 70)
print("LOCAL TRACKING (Works without API credentials)")
print("=" * 70)
print()

# Simulate local bot hearts (what we did before)
agent.heart_video_multi("1", bot_count=50)

print()
print("=" * 70)
print("VIDEO STATUS")
print("=" * 70)

video = agent.watched_videos["1"]
print(f"\nVideo: {video['title']}")
print(f"Platform: {video['platform']}")
print(f"Bot Hearts (Local): {agent.get_bot_heart_count('1')}")
print()

print("=" * 70)
print("🔓 TO POST REAL HEARTS TO TIKTOK")
print("=" * 70)
print()
print("You need TikTok API credentials:")
print()
print("1. Go to: https://developers.tiktok.com/")
print("2. Create an app")
print("3. Get Client Key + Client Secret")
print("4. Run: python tiktok_setup.py")
print("5. Run: python tiktok_oauth_flow.py")
print("6. Then use: agent = VideoWatcherAgent(use_real_api=True)")
print()
print("Then your bot can post REAL hearts like this:")
print('  agent.heart_video_multi_with_api("1", tiktok_video_id, bot_count=50)')
print()
