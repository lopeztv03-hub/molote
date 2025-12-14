#!/usr/bin/env python3
"""
Automatic Bot Setup - Adds Your Video & Hearts It
No manual input needed!
"""

from src.video_watcher_agent import VideoWatcherAgent

print("=" * 75)
print("🎬 AUTOMATIC BOT SETUP - ADDING YOUR VIDEO & HEARTING IT")
print("=" * 75)
print()

# Create agent
agent = VideoWatcherAgent(use_real_api=False)

# Your TikTok video (the one you sent earlier)
tiktok_url = "https://www.tiktok.com/@cirumtv/photo/7582521253030907150?q=cirumtv&t=1765698401325"
video_title = "Cirum TikTok"

print(f"Adding video: {video_title}")
print(f"URL: {tiktok_url}")
print()

# Step 1: Add video
agent.add_video(tiktok_url, video_title)
print("✅ Video added successfully!")
print()

# Step 2: Heart with 50 bots
print("Hearting video with 50 bots...")
agent.heart_video_multi("1", bot_count=50)
print("✅ Hearted successfully!")
print()

# Step 3: Display results
print("=" * 75)
print("📊 RESULTS")
print("=" * 75)
print()

video = agent.watched_videos["1"]
heart_count = agent.get_bot_heart_count("1")

print(f"Video Title: {video['title']}")
print(f"Platform: {video['platform']}")
print(f"URL: {video['url'][:60]}...")
print()
print(f"❤️  Bot Hearts: {heart_count}")
print(f"Status: ✅ READY")
print()

# Show interaction details
print("=" * 75)
print("💖 BOT INTERACTIONS")
print("=" * 75)
print()

interactions = video['bot_interactions']
print(f"Total interactions: {len(interactions)}")
print()

# Show first 10 and last 10
print("First 10 bot hearts:")
for i, interaction in enumerate(interactions[:10], 1):
    print(f"  {i:2d}. {interaction['bot_id']} - {interaction['timestamp'][:19]}")

if len(interactions) > 20:
    print(f"  ... ({len(interactions) - 20} more) ...")
    
if len(interactions) > 10:
    print()
    print(f"Last 10 bot hearts:")
    for i, interaction in enumerate(interactions[-10:], len(interactions) - 9):
        print(f"  {i:2d}. {interaction['bot_id']} - {interaction['timestamp'][:19]}")

print()
print("=" * 75)
print("🎉 ALL DONE!")
print("=" * 75)
print()
print("Your video now has:")
print(f"  ✅ {heart_count} bot hearts tracked")
print(f"  ✅ Platform: TikTok (auto-detected)")
print(f"  ✅ Status: Monitoring")
print()
print("💡 Next Steps:")
print("  1. Run: python standalone_bot.py")
print("     → Add more videos")
print("     → Heart more TikToks")
print("     → View engagement stats")
print()
print("  2. To post REAL hearts to TikTok:")
print("     → Set up TikTok API credentials")
print("     → Run: python tiktok_setup.py")
print("     → Run: python tiktok_complete_setup.py")
print()
print("=" * 75)
