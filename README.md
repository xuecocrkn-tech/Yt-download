# Simple YouTube Downloader

A lightweight Python script to download YouTube Videos (High Quality), Thumbnails, or MP3 Audio. 
Works on **Android (Termux)** and **PC (Windows/Linux/Mac)**.

---

## 🚀 Features

- **Smart Device Detection:** Optimized paths for Phone (Gallery) or PC.
- **High Quality:** Automatically merges the best video and audio streams.
- **Shorts Support:** Fully compatible with YouTube Shorts.
- **Thumbnails:** Extracts high-resolution thumbnails in JPG format.
- **Audio Extraction:** Convert videos directly to high-quality MP3 (192kbps).

---

## 🛠️ Installation

### 1. Prerequisites
- **Python 3.x** installed.
- **FFmpeg** (Required for high-quality video merging and MP3 extraction).
  - *Linux:* `sudo apt install ffmpeg`
  - *Mac:* `brew install ffmpeg`
  - *Android (Termux):* `pkg install ffmpeg`

### 2. Clone & Install Dependencies
```bash
git clone https://github.com/xuecocrkn-tech/Yt-download.git
cd Yt-download
pip install -r requirements.txt
```

---

## 📖 How to Use

Run the script and follow the interactive prompts:

```bash
python d.py
```

Alternatively, you can pass the URL directly as an argument:

```bash
python d.py "https://www.youtube.com/watch?v=example"
```

### Options:
1. **Select Device:** Choose between Phone (saves to `/sdcard/Download`) or PC (saves to current folder).
2. **Select Action:** 
   - `1`: Download Video (MP4)
   - `2`: Download Thumbnail (JPG)
   - `3`: Download Audio (MP3)

---

## 📝 License
This project is open-source. Feel free to use and modify it!
