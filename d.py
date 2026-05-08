import yt_dlp
import sys
import os

def run():
    # 1. Device Selection
    print("📱 Select Device:")
    print("1. Phone (Save to /sdcard/Download)")
    print("2. PC (Save to current folder)")
    device = input("Enter your choice (1 or 2): ")

    # Set save path
    if device == '1':
        save_path = "/sdcard/Download%(title)s.%(ext)s"
    else:
        save_path = "%(title)s.%(ext)s"

    # 2. Get URL
    url = sys.argv[1] if len(sys.argv) > 1 else input("\n🔗 Paste link: ").strip()
    if not url: return

    # 3. Action Selection
    print("\n🎬 What would you like to download?")
    print("1. Video (Best quality MP4)")
    print("2. Thumbnail (JPG Image)")
    print("3. Audio/Music (MP3)")  # <-- Добавлен новый пункт
    action = input("Enter your choice (1, 2, or 3): ")

    opts = {}

    if action == '1':
        opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': save_path,
            'merge_output_format': 'mp4',
            # Use aria2 for speed if installed
            'external_downloader': 'aria2c' if os.popen('command -v aria2c').read() else None
        }
        print("\n🚀 Downloading video...")
    
    elif action == '2':
        opts = {
            'writethumbnail': True,
            'skip_download': True,
            'outtmpl': save_path,
            'postprocessors': [{
                'key': 'FFmpegThumbnailsConvertor',
                'format': 'jpg',
            }],
        }
        print("\n🖼️  Downloading thumbnail...")

    # <-- Блок для скачивания музыки
    elif action == '3':
        opts = {
            'format': 'bestaudio/best',
            'outtmpl': save_path,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
        print("\n🎵 Downloading audio (MP3)...")
        print("⚠️  Note: FFmpeg must be installed for audio conversion.")
    
    else:
        print("❌ Invalid choice.")
        return

    try:
        with yt_dlp.YoutubeDL(opts) as ydl:
            ydl.download([url])
        
        location = "Downloads folder" if device == '1' else "current folder"
        file_type = "Video" if action == '1' else "Thumbnail" if action == '2' else "Audio"
        print(f"\n✅ Done! {file_type} saved in your {location}.")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        if action == '3':
            print("💡 Tip: If you are downloading audio, make sure FFmpeg is installed.")

if __name__ == "__main__":
    run()
