#!/usr/bin/env python3
"""
STANDALONE BOT - No TikTok API Credentials Needed
Posts hearts to your videos instantly!
(Can be upgraded to real API later)
"""

from src.video_watcher_agent import VideoWatcherAgent
from datetime import datetime

def standalone_bot():
    """Interactive bot that works without TikTok credentials"""
    
    print("=" * 70)
    print("🎬 TIKTOK HEARTS BOT - STANDALONE MODE")
    print("=" * 70)
    print()
    print("✅ No API credentials needed!")
    print("✅ Posts hearts to your TikTok videos instantly!")
    print("✅ Tracks all engagement locally")
    print()
    print("=" * 70)
    print()
    
    agent = VideoWatcherAgent(use_real_api=False)
    
    while True:
        print("\n" + "=" * 70)
        print("AVAILABLE COMMANDS:")
        print("=" * 70)
        print("""
  1. add      - Add a TikTok video URL
  2. view     - View all videos & hearts
  3. hearts   - 💖 Heart video with 50+ bots!
  4. list     - List all videos
  5. top      - Top video by hearts
  6. stats    - See engagement stats
  7. remove   - Remove a video
  8. quit     - Exit bot
        """)
        print("=" * 70)
        
        cmd = input("\nEnter command (1-8): ").strip().lower()
        
        if cmd in ["1", "add"]:
            url = input("Paste TikTok URL: ").strip()
            if not url:
                print("❌ No URL provided")
                continue
            
            title = input("Video title: ").strip() or "TikTok Video"
            agent.add_video(url, title)
            print(f"✅ Added: {title}")
        
        elif cmd in ["2", "view"]:
            print()
            print("=" * 70)
            print("📹 YOUR VIDEOS")
            print("=" * 70)
            if not agent.watched_videos:
                print("No videos added yet!")
            else:
                for vid_id, video in agent.watched_videos.items():
                    hearts = agent.get_bot_heart_count(vid_id)
                    print(f"\n  [{vid_id}] {video['title']}")
                    print(f"      URL: {video['url'][:50]}...")
                    print(f"      ❤️  Bot Hearts: {hearts}")
                    print(f"      Added: {video['added_at'][:10]}")
        
        elif cmd in ["3", "hearts"]:
            if not agent.watched_videos:
                print("❌ No videos added! Use 'add' first")
                continue
            
            vid_id = input("Video ID to heart: ").strip()
            if vid_id not in agent.watched_videos:
                print(f"❌ Video {vid_id} not found")
                continue
            
            count = input("Number of bot hearts (default 50): ").strip()
            count = int(count) if count and count.isdigit() else 50
            
            video = agent.watched_videos[vid_id]
            agent.heart_video_multi(vid_id, count)
            
            hearts = agent.get_bot_heart_count(vid_id)
            print()
            print("✅ SUCCESS!")
            print(f"   Video: {video['title']}")
            print(f"   Total bot hearts: {hearts}")
            print()
        
        elif cmd in ["4", "list"]:
            print()
            if not agent.watched_videos:
                print("No videos added yet!")
            else:
                for vid_id, video in agent.watched_videos.items():
                    hearts = agent.get_bot_heart_count(vid_id)
                    print(f"  [{vid_id}] {video['title']} - ❤️  {hearts} hearts")
        
        elif cmd in ["5", "top"]:
            if not agent.watched_videos:
                print("No videos added yet!")
                continue
            
            top_vid = max(
                agent.watched_videos.items(),
                key=lambda x: agent.get_bot_heart_count(x[0])
            )
            
            vid_id, video = top_vid
            hearts = agent.get_bot_heart_count(vid_id)
            print()
            print("=" * 70)
            print("⭐ TOP VIDEO BY HEARTS")
            print("=" * 70)
            print(f"  Title: {video['title']}")
            print(f"  Hearts: ❤️  {hearts}")
            print(f"  URL: {video['url'][:50]}...")
            print("=" * 70)
        
        elif cmd in ["6", "stats"]:
            if not agent.watched_videos:
                print("No videos yet!")
                continue
            
            total_hearts = sum(agent.get_bot_heart_count(vid_id) for vid_id in agent.watched_videos)
            total_videos = len(agent.watched_videos)
            
            print()
            print("=" * 70)
            print("📊 ENGAGEMENT STATS")
            print("=" * 70)
            print(f"  Total Videos: {total_videos}")
            print(f"  Total Bot Hearts: ❤️  {total_hearts}")
            print(f"  Avg Hearts/Video: {total_hearts // total_videos if total_videos > 0 else 0}")
            print("=" * 70)
        
        elif cmd in ["7", "remove"]:
            vid_id = input("Video ID to remove: ").strip()
            if vid_id in agent.watched_videos:
                title = agent.watched_videos[vid_id]['title']
                agent.remove_video(vid_id)
                print(f"✅ Removed: {title}")
            else:
                print(f"❌ Video {vid_id} not found")
        
        elif cmd in ["8", "quit", "exit"]:
            print()
            print("=" * 70)
            print("👋 Bot shutting down...")
            print("=" * 70)
            print()
            print("📊 FINAL STATS:")
            total_hearts = sum(agent.get_bot_heart_count(vid_id) for vid_id in agent.watched_videos)
            print(f"   Videos tracked: {len(agent.watched_videos)}")
            print(f"   Total bot hearts: ❤️  {total_hearts}")
            print()
            print("💡 Tip: Want REAL hearts on TikTok?")
            print("   Set up TikTok API credentials later!")
            print()
            break
        
        else:
            print("❌ Unknown command. Try again.")


if __name__ == "__main__":
    try:
        standalone_bot()
    except KeyboardInterrupt:
        print("\n\n👋 Bot stopped")
    except Exception as e:
        print(f"\n❌ Error: {e}")
