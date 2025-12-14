#!/usr/bin/env python3
"""Quick script to add a video and heart it with bots"""

from src.video_watcher_agent import VideoWatcherAgent

# Create agent
agent = VideoWatcherAgent()

# Add the TikTok video
url = "https://www.tiktok.com/@cirumtv/photo/7582521253030907150?q=cirumtv&t=1765698401325"
title = "Cirum TikTok"

print("=" * 60)
print("🎬 VIDEO WATCHER BOT - QUICK ADD & HEART")
print("=" * 60)
print()

# Add video
agent.add_video(url, title)

# Heart with 50 bots
agent.heart_video_multi("1", bot_count=50)

# Display the video
print()
print("=" * 60)
print("📹 VIDEO DETAILS")
print("=" * 60)
video = agent.watched_videos["1"]
print(f"\n  [1] ❤️ {video['title']}")
print(f"      Platform:............ {video['platform']}")
print(f"      URL:................. {video['url'][:50]}...")
print(f"      Bot Hearted:......... Yes ❤️")
print(f"      Bot Hearts Count:.... 50")
print(f"      Bot Interactions:... {len(video['bot_interactions'])}")
for interaction in video['bot_interactions']:
    print(f"        • {interaction['action'].upper()} by {interaction['bot_id']} at {interaction['timestamp'][:19]}")
print()
print("=" * 60)
print("✅ Video added and 50 bots hearted successfully!")
print("=" * 60)
