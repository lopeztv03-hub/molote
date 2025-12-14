"""
Main entry point for multi-agent social media bot system
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


def main():
    """Initialize and run the social media bot system"""
    
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
    
    manager.register_agent(twitter_agent)
    manager.register_agent(instagram_agent)
    manager.register_agent(tiktok_agent)
    manager.register_agent(youtube_agent)
    manager.register_agent(facebook_agent)
    manager.register_agent(linkedin_agent)
    manager.register_agent(summary_agent)
    
    print("\n🤖 Social Media Bot System Initialized")
    print("   Available Agents:")
    for agent_name in manager.list_agents():
        print(f"     • {agent_name}")
    
    # Display report
    print(manager.get_report())
    
    # Run once to display all social media views
    manager.run_once()
    
    # Uncomment below to run with scheduled updates every 60 seconds
    # manager.schedule_updates(interval=60)
    
    # Example: Disable specific agents
    # manager.disable_agent("FacebookViewAgent")
    # manager.run_once()


if __name__ == "__main__":
    main()

