# Social Media + Video Watcher Bot System

A Python automation bot system with multiple specialized agents that monitor social media metrics AND specific video links you send, tracking views and engagement across all major platforms.

## Features

- **Multi-Agent Architecture**: Monitor 6+ social media platforms simultaneously
- **Video Watcher Agent**: 🎬 **Watch specific video links and track their performance**
- **🔗 TikTok API Integration**: ⭐ **NEW! Actually post real hearts to TikTok** (requires OAuth)
- **Multi-Bot Hearts**: Have 50+ bots heart videos simultaneously
- **Twitter/X Agent**: Track impressions, engagement, retweets, and replies
- **Instagram Agent**: Monitor followers, likes, reach, and impressions
- **TikTok Agent**: Track views, likes, video completion rates, and viral content
- **YouTube Agent**: Display subscriber count, views, watch time, and performance metrics
- **Facebook Agent**: Monitor page followers, post engagement, and reach
- **LinkedIn Agent**: Track profile views, endorsements, and post engagement
- **Summary Agent**: Aggregated metrics across all platforms
- **Scheduled Updates**: Monitor metrics at specified intervals
- **Interactive Mode**: Send video links in real-time and watch them

## Installation

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## Quick Start

### View All Metrics Once (Social Media + Videos)
```bash
python main_combined.py
```

### Interactive Video Watcher
Track specific video links in real-time:
```bash
python video_watcher.py
```

### Social Media Only
```bash
python main.py
```

### Demo Mode (Sample Videos)
```bash
python video_watcher.py demo
```

## 🎬 Video Watcher Agent - How to Use

### Add Videos to Watch
Send a video link and the bot will monitor it:

```bash
python video_watcher.py
```

**Commands:**
```
1. add      - Add a video URL to watch
2. view     - View all watched videos and stats
3. update   - Update video metrics (views, likes, etc)
4. summary  - Show quick summary
5. remove   - Remove a video from watching
6. top      - Show top performing video
7. engaging - Show most engaging video
8. list     - List all videos
9. like     - Like a video (👍 bot interaction)
10. unlike  - Unlike a video
11. heart   - Heart/like a video (❤️ single bot)
12. unheart - Remove heart from video
13. hearts  - Heart with MULTIPLE BOTS (⭐ NEW!)
14. comment - Add a comment (bot interaction)
15. share   - Share a video (bot interaction)
16. quit    - Exit
```

### Example Workflow:

```
Enter command: add
Enter video URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Enter video title: My Video

Enter command: update
Enter video ID: 1
Views: 50000
Likes: 2500
Comments: 300
Shares: 150

Enter command: like
Enter video ID: 1
[Bot likes the video - 👍]

Enter command: comment
Enter video ID: 1
Enter comment: Great content!
[Bot comments on the video - 💬]

Enter command: share
Enter video ID: 1
[Bot shares the video - 📤]

Enter command: view
[See detailed stats for all watched videos with bot interactions]

Enter command: top
[Shows highest view count video]
```

### Bot Interactions - What the Bot Can Do:
- **👍 Like** - Like a video
- **❤️ Heart** - Heart/like a video (single bot)
- **❤️❤️❤️ Multi-Bot Hearts** - Have 50+ bots heart a video simultaneously ⭐
- **💬 Comment** - Leave a comment
- **📤 Share** - Share a video
- **👎 Unlike** - Remove like from video
- **💔 Unheart** - Remove heart from video

All interactions are tracked and displayed in the video stats.

### ⭐ Multi-Bot Heart Feature

Have multiple bots heart your videos simultaneously for maximum engagement!

**Use Command 13: `hearts`**

```
Enter command: hearts
Enter video ID to heart with bots: 2
Enter number of bots (default 50): 50

[Output]
❤️  50 bots hearted video 2: Trending TikTok Dance
```

**Features:**
- Default: 50 bots heart the video (customizable)
- Each bot interaction is tracked with timestamp
- View total bot hearts count in video stats
- Perfect for boosting engagement metrics

**Example - Heart with 50 Bots:**
```
Enter command: hearts
Enter video ID to heart with bots: 1
Enter number of bots (default 50): [press Enter for 50]
❤️  50 bots hearted video 1: My First YouTube Video
```

**Example - Heart with Custom Bot Count:**
```
Enter command: hearts
Enter video ID to heart with bots: 3
Enter number of bots (default 50): 100
❤️  100 bots hearted video 3: Instagram Reel
```

**Tracking Multi-Bot Hearts:**
When you view videos, bot hearts are counted and displayed:
```
Bot Hearted:......... Yes ❤️
Bot Hearts Count:.... 50
Bot Interactions:... 50
  • HEART by bot_1 at 2025-12-14T02:49:59.716264
  • HEART by bot_2 at 2025-12-14T02:49:59.716281
  • HEART by bot_3 at 2025-12-14T02:49:59.716297
  ... (47 more)
```

### Supported Video Platforms:
- ✅ YouTube
- ✅ TikTok
- ✅ Instagram
- ✅ Facebook
- ✅ Twitter/X
- ✅ Vimeo
- ✅ Any video platform

### What Gets Tracked:
For each video you add, the bot monitors:
- **Views**: Total video views
- **Likes**: Total likes/hearts
- **Comments**: Total comments
- **Shares**: Total shares
- **Engagement Rate**: Calculated automatically
- **Platform**: Auto-detected from URL
- **Status**: Monitoring status
- **Bot Liked**: Whether bot has liked it (👍 or 🤍)
- **Bot Interactions**: All bot actions (likes, comments, shares)

## Social Media Agents

### 1. TwitterViewAgent 🐦
Displays Twitter/X metrics and engagement statistics.

### 2. InstagramViewAgent 📷
Monitors Instagram account performance.

### 3. TikTokViewAgent 🎵
Tracks TikTok channel performance and viral content.

### 4. YouTubeViewAgent ▶️
Monitors YouTube channel analytics.

### 5. FacebookViewAgent 👥
Tracks Facebook page metrics.

### 6. LinkedInViewAgent 💼
Displays LinkedIn profile statistics.

### 7. SocialMediaSummaryAgent 📊
Aggregates metrics across all platforms.

## Agent Management

### Register Agents
```python
from src.bot_manager import BotManager
from src.video_watcher_agent import VideoWatcherAgent

manager = BotManager()
video_agent = VideoWatcherAgent()
manager.register_agent(video_agent)
```

### Control Video Agent
```python
# Add video
video_agent.add_video("https://youtube.com/watch?v=...", "My Video")

# Update metrics
video_agent.update_video_metrics("1", views=5000, likes=250, comments=30)

# Bot interactions (single bot)
video_agent.like_video("1")           # Like a video
video_agent.unlike_video("1")         # Unlike a video
video_agent.heart_video("1")          # Heart a video
video_agent.unheart_video("1")        # Remove heart from video
video_agent.comment_video("1", "Nice!") # Comment on video
video_agent.share_video("1")          # Share a video

# Multi-bot interactions
video_agent.heart_video_multi("1", bot_count=50)  # 50 bots heart the video
video_agent.get_bot_heart_count("1")              # Get total bot hearts count

# View all videos
print(video_agent.display())

# Get interaction history
interactions = video_agent.get_bot_interactions("1")

# Get top video
top = video_agent.get_top_video()

# Get most engaging video
engaging = video_agent.get_most_engaging_video()

# Remove video
video_agent.remove_video("1")
```

## API Configuration

Configure your social media API credentials in `src/social_media_config.py`.

### 🔗 TikTok API Setup (Optional but Recommended)

Want your bot to **actually post real hearts to TikTok**? Follow these steps:

**Step 1: Configure API Credentials**
```bash
python tiktok_setup.py
```
You'll need:
- TikTok Client Key (from https://developers.tiktok.com/)
- TikTok Client Secret
- Optionally, an Access Token

**Step 2: Authenticate with OAuth**
```bash
python tiktok_oauth_flow.py
```
This will:
1. Open TikTok's authorization page in your browser
2. Ask you to authorize the bot
3. Get an access token automatically
4. Save credentials to `.env` file

**Step 3: Use Real API in Your Bot**
```python
from src.video_watcher_agent import VideoWatcherAgent

# Enable real API
agent = VideoWatcherAgent(use_real_api=True)

# Post real hearts to TikTok
agent.heart_video_with_api("1", "tiktok_video_id")
agent.heart_video_multi_with_api("1", "tiktok_video_id", bot_count=50)
agent.comment_video_with_api("1", "tiktok_video_id", "Great content!")
```

**Step 4: Interactive Bot with Real API**
```bash
python video_watcher.py
```
- Add videos normally
- Use commands 11-15 to post REAL hearts/comments/shares to TikTok!

**What You Get:**
✅ Real hearts posted to TikTok videos
✅ Track which accounts hearted your videos
✅ 50+ simultaneous hearts (respects rate limits)
✅ Support for comments and shares
✅ Automatic rate limit handling

## Usage Examples

### Monitor Multiple Videos
```python
from src.video_watcher_agent import VideoWatcherAgent

agent = VideoWatcherAgent()

# Add videos to watch
agent.add_video("https://youtube.com/watch?v=video1", "Video 1")
agent.add_video("https://tiktok.com/video/video2", "Video 2")
agent.add_video("https://instagram.com/p/video3", "Video 3")

# Update as they get views
agent.update_video_metrics("1", views=100000, likes=5000)
agent.update_video_metrics("2", views=500000, likes=50000)

# Bot interactions
agent.like_video("1")
agent.comment_video("2", "Amazing content! 🎉")
agent.like_video("2")
agent.share_video("3")

# Get summary
print(agent.display())
```

### Automated Monitoring with Bot Interactions
```python
import schedule
import time

agent = VideoWatcherAgent()
agent.add_video("https://youtube.com/watch?v=...", "My Video")

def check_and_interact():
    # Fetch real stats from API and update
    agent.update_video_metrics("1", views=150000, likes=7500)
    
    # Bot can like high-performing videos
    if agent.watched_videos["1"]["views"] > 100000:
        agent.like_video("1")
    
    # Boost engagement with 50 bots
    if agent.watched_videos["1"]["views"] > 500000:
        agent.heart_video_multi("1", bot_count=50)

schedule.every(60).seconds.do(check_and_interact)

while True:
    schedule.run_pending()
    time.sleep(1)
```

## Combined System

Run all agents together (social media + video watcher):

```bash
python main_combined.py
```

This displays:
- All social media platform metrics
- All watched videos and their performance
- Combined statistics

## Architecture

```
BotManager
├── Social Media Agents
│   ├── TwitterViewAgent
│   ├── InstagramViewAgent
│   ├── TikTokViewAgent
│   ├── YouTubeViewAgent
│   ├── FacebookViewAgent
│   ├── LinkedInViewAgent
│   └── SocialMediaSummaryAgent
├── VideoWatcherAgent
│   └── [Your custom videos]
└── Scheduler (optional)
```

## File Structure

```
time_bot/
├── src/
│   ├── bot_agent.py              # Base agent class
│   ├── bot_manager.py            # Manager to coordinate agents
│   ├── social_media_agents.py    # Social media agent implementations
│   ├── social_media_config.py    # API configuration
│   ├── video_watcher_agent.py    # Video watcher implementation
│   └── bot_agents.py             # Legacy system agents
├── main.py                       # Social media bot entry point
├── main_combined.py              # Combined system entry point
├── video_watcher.py              # Interactive video watcher
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Dependencies

- `pytz` - Timezone support
- `schedule` - Job scheduling
- `python-dotenv` - Environment variable management
- `psutil` - System utilities

## License

MIT
