"""
Video Watcher Bot - Monitor specific video links for views and engagement
Interactive bot that watches videos you send
"""

from src.bot_manager import BotManager
from src.video_watcher_agent import VideoWatcherAgent


def main():
    """Initialize and run the video watcher bot"""
    
    print("\n" + "="*70)
    print("🎬 VIDEO WATCHER BOT")
    print("="*70)
    print("This bot monitors video links you send and tracks their performance!")
    print("="*70 + "\n")
    
    # Create bot manager
    manager = BotManager()
    
    # Create video watcher agent
    video_agent = VideoWatcherAgent()
    manager.register_agent(video_agent)
    
    print("Available Commands:")
    print("  1. add      - Add a video to watch")
    print("  2. view     - View all watched videos")
    print("  3. update   - Update video metrics")
    print("  4. summary  - Show summary of videos")
    print("  5. remove   - Remove a video")
    print("  6. top      - Show top performing video")
    print("  7. engaging - Show most engaging video")
    print("  8. list     - List all videos")
    print("  9. like     - Like a video (👍 bot interaction)")
    print("  10. unlike  - Unlike a video")
    print("  11. heart   - Heart a video (❤️  bot interaction)")
    print("  12. unheart - Unheart a video")
    print("  13. hearts  - Heart with multiple bots (50+ bots)")
    print("  14. comment - Comment on a video")
    print("  15. share   - Share a video")
    print("  16. quit    - Exit\n")
    
    while True:
        command = input("Enter command (1-9): ").strip().lower()
        
        if command in ["1", "add"]:
            url = input("Enter video URL: ").strip()
            title = input("Enter video title (optional): ").strip() or None
            video_agent.add_video(url, title)
            
        elif command in ["2", "view"]:
            print(video_agent.display())
            
        elif command in ["3", "update"]:
            video_id = input("Enter video ID to update: ").strip()
            views = input("Views (or press Enter to skip): ").strip()
            likes = input("Likes (or press Enter to skip): ").strip()
            comments = input("Comments (or press Enter to skip): ").strip()
            shares = input("Shares (or press Enter to skip): ").strip()
            
            video_agent.update_video_metrics(
                video_id,
                views=int(views) if views else None,
                likes=int(likes) if likes else None,
                comments=int(comments) if comments else None,
                shares=int(shares) if shares else None
            )
            print(f"✓ Updated video {video_id}")
            
        elif command in ["4", "summary"]:
            print(video_agent.display_summary())
            
        elif command in ["5", "remove"]:
            video_id = input("Enter video ID to remove: ").strip()
            if video_agent.remove_video(video_id):
                print(f"✓ Video {video_id} removed")
            else:
                print(f"✗ Video {video_id} not found")
                
        elif command in ["6", "top"]:
            top = video_agent.get_top_video()
            if top:
                print(f"\n⭐ Top Video by Views: {top['title']}")
                print(f"   Views: {top['views']:,}")
            else:
                print("No videos to show")
                
        elif command in ["7", "engaging"]:
            engaging = video_agent.get_most_engaging_video()
            if engaging:
                print(f"\n🔥 Most Engaging Video: {engaging['title']}")
                print(f"   Engagement Rate: {engaging['engagement_rate']:.2f}%")
            else:
                print("No videos to show")
                
        elif command in ["8", "list"]:
            videos = video_agent.list_videos()
            if videos:
                print(f"\nVideos Being Watched ({len(videos)}):")
                for i, v in enumerate(videos, 1):
                    print(f"  {i}. {v['title']} ({v['platform']})")
            else:
                print("No videos being watched")
        
        elif command in ["9", "like"]:
            video_id = input("Enter video ID to like: ").strip()
            video_agent.like_video(video_id)
        
        elif command in ["10", "unlike"]:
            video_id = input("Enter video ID to unlike: ").strip()
            video_agent.unlike_video(video_id)
        
        elif command in ["11", "heart"]:
            video_id = input("Enter video ID to heart: ").strip()
            video_agent.heart_video(video_id)
        
        elif command in ["12", "unheart"]:
            video_id = input("Enter video ID to unheart: ").strip()
            video_agent.unheart_video(video_id)
        
        elif command in ["13", "hearts"]:
            video_id = input("Enter video ID to heart with bots: ").strip()
            num_bots = input("Enter number of bots (default 50): ").strip()
            num_bots = int(num_bots) if num_bots and num_bots.isdigit() else 50
            video_agent.heart_video_multi(video_id, num_bots)
        
        elif command in ["14", "comment"]:
            video_id = input("Enter video ID to comment on: ").strip()
            comment = input("Enter comment: ").strip()
            video_agent.comment_video(video_id, comment)
        
        elif command in ["14", "share"]:
            video_id = input("Enter video ID to share: ").strip()
            video_agent.share_video(video_id)
                
        elif command in ["15", "quit", "exit"]:
            print("\n👋 Bot shutting down...")
            break
            
        else:
            print("Invalid command. Please try again.")
        
        print()


def demo_mode():
    """Run demo with sample videos"""
    
    print("\n" + "="*70)
    print("🎬 VIDEO WATCHER BOT - DEMO MODE")
    print("="*70 + "\n")
    
    # Create bot manager
    manager = BotManager()
    
    # Create video watcher agent
    video_agent = VideoWatcherAgent()
    manager.register_agent(video_agent)
    
    # Add sample videos
    print("Adding sample videos to watch...\n")
    
    video_agent.add_video(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "My First YouTube Video"
    )
    video_agent.update_video_metrics("1", views=152000, likes=8500, comments=1200, shares=450)
    
    video_agent.add_video(
        "https://www.tiktok.com/@user/video/1234567890",
        "Trending TikTok Dance"
    )
    video_agent.update_video_metrics("2", views=540000, likes=98000, comments=5600, shares=2300)
    
    video_agent.add_video(
        "https://www.instagram.com/p/ABC123DEF456/",
        "Instagram Reel"
    )
    video_agent.update_video_metrics("3", views=89000, likes=4500, comments=320, shares=210)
    
    # Bot interactions
    print("\nBot interactions:\n")
    video_agent.like_video("1")
    video_agent.heart_video_multi("2", 50)  # 50 bots heart the video
    video_agent.comment_video("2", "Great content! Love this! 🎉")
    video_agent.like_video("2")
    video_agent.heart_video_multi("3", 25)  # 25 bots heart this one
    video_agent.share_video("3")
    
    # Display results
    print(video_agent.display())
    print(video_agent.display_summary())
    
    # Show top videos
    top = video_agent.get_top_video()
    most_engaging = video_agent.get_most_engaging_video()
    
    print(f"\n⭐ Top Video by Views: {top['title']}")
    print(f"   Views: {top['views']:,}\n")
    
    print(f"🔥 Most Engaging: {most_engaging['title']}")
    print(f"   Engagement Rate: {most_engaging['engagement_rate']:.2f}%\n")


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "demo":
        demo_mode()
    else:
        main()
