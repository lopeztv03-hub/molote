"""
Combined Bot System - Social Media Agents + Video Watcher
"""

from src.bot_manager import BotManager
from src.social_media_agents import (
    TwitterViewAgent,
    InstagramViewAgent,
    TikTokViewAgent,
    YouTubeViewAgent,
    FacebookViewAgent,
    LinkedInViewAgent,
    SocialMediaSummaryAgent
)
from src.video_watcher_agent import VideoWatcherAgent


def main():
    """Initialize and run the combined bot system"""
    
    print("\n" + "█"*70)
    print("█  🎬 SOCIAL MEDIA + VIDEO WATCHER BOT SYSTEM")
    print("█"*70 + "\n")
    
    # Create bot manager
    manager = BotManager()
    
    # Create and register social media agents
    twitter_agent = TwitterViewAgent()
    instagram_agent = InstagramViewAgent()
    tiktok_agent = TikTokViewAgent()
    youtube_agent = YouTubeViewAgent()
    facebook_agent = FacebookViewAgent()
    linkedin_agent = LinkedInViewAgent()
    summary_agent = SocialMediaSummaryAgent()
    
    # Create and register video watcher agent
    video_agent = VideoWatcherAgent()
    
    manager.register_agent(twitter_agent)
    manager.register_agent(instagram_agent)
    manager.register_agent(tiktok_agent)
    manager.register_agent(youtube_agent)
    manager.register_agent(facebook_agent)
    manager.register_agent(linkedin_agent)
    manager.register_agent(summary_agent)
    manager.register_agent(video_agent)
    
    print("   Available Agents:")
    for agent_name in manager.list_agents():
        print(f"     • {agent_name}")
    
    # Display report
    print(manager.get_report())
    
    # Display all views
    manager.run_once()
    
    # Demo: Add some videos to the video watcher
    print("\n\n" + "█"*70)
    print("█  📹 ADDING SAMPLE VIDEOS TO WATCH")
    print("█"*70 + "\n")
    
    video_agent.add_video(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "My Latest YouTube Video"
    )
    video_agent.update_video_metrics("1", views=250000, likes=12500, comments=1800, shares=650)
    
    video_agent.add_video(
        "https://www.tiktok.com/@user/video/1234567890",
        "Viral TikTok Content"
    )
    video_agent.update_video_metrics("2", views=850000, likes=156000, comments=8900, shares=4200)
    
    video_agent.add_video(
        "https://www.instagram.com/p/ABC123DEF456/",
        "Instagram Story Highlight"
    )
    video_agent.update_video_metrics("3", views=145000, likes=7200, comments=520, shares=350)
    
    # Display video watcher results
    print(video_agent.display())
    print(video_agent.display_summary())
    
    print("\n" + "█"*70)
    print("█  SYSTEM READY FOR MONITORING")
    print("█"*70)
    print("\nNext Steps:")
    print("  • Run 'python video_watcher.py' for interactive video tracking")
    print("  • Add your API credentials to src/social_media_config.py")
    print("  • Uncomment scheduling in main.py for continuous monitoring")
    print("█"*70 + "\n")
    
    # Uncomment below to run with scheduled updates
    # manager.schedule_updates(interval=60)


if __name__ == "__main__":
    main()
