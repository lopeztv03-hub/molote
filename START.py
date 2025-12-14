#!/usr/bin/env python3
"""
🚀 TIKTOK BOT LAUNCHER
Choose which bot mode to run
"""

import subprocess
import sys

def main():
    print("""
╔════════════════════════════════════════════════════════════════╗
║              🎬 TIKTOK BOT LAUNCHER - OPTION C                 ║
║                  (Hybrid: Mock API Now, Real Later)            ║
╚════════════════════════════════════════════════════════════════╝

Your bot has 3 modes. Pick one:

""")
    
    print("1️⃣  AUTOMATIC MODE (Recommended)")
    print("    └─ Fully automated")
    print("    └─ No user input")
    print("    └─ Runs in ~5 seconds")
    print("    └─ Command: full_auto_bot.py")
    print()
    
    print("2️⃣  INTERACTIVE MODE")
    print("    └─ Manual control")
    print("    └─ Add videos yourself")
    print("    └─ Heart on demand")
    print("    └─ Command: standalone_bot.py")
    print()
    
    print("3️⃣  DEMO MODE")
    print("    └─ See sample videos")
    print("    └─ View statistics")
    print("    └─ Test all features")
    print("    └─ Command: video_watcher.py demo")
    print()
    
    print("4️⃣  EXIT")
    print()
    
    choice = input("Choose mode (1-4): ").strip()
    
    print()
    print("=" * 65)
    
    if choice == "1":
        print("🤖 Starting AUTOMATIC MODE...")
        print("=" * 65)
        print()
        subprocess.run([sys.executable, "full_auto_bot.py"])
        
    elif choice == "2":
        print("💬 Starting INTERACTIVE MODE...")
        print("=" * 65)
        print()
        subprocess.run([sys.executable, "standalone_bot.py"])
        
    elif choice == "3":
        print("📺 Starting DEMO MODE...")
        print("=" * 65)
        print()
        subprocess.run([sys.executable, "video_watcher.py", "demo"])
        
    elif choice == "4":
        print("👋 Exiting...")
        print()
        sys.exit(0)
        
    else:
        print("❌ Invalid choice")
        sys.exit(1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Bot stopped")
        sys.exit(0)
