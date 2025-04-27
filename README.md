# 📹 YouTube Downloader (Python + yt-dlp)

A simple, clean YouTube downloader built using **Python** and **yt-dlp**, with optional audio-only extraction, resolution selection, and a live progress bar.

---

## 📊 Features

- 📥 Download YouTube videos in Best Quality (default)
- 🎵 Download Audio Only as MP3 (auto-convert using FFmpeg)
- 🎞️ Download 720p resolution videos if available
- 📊 Live Progress Bar (shows percentage while downloading)
- 🌐 Auto-detect if `ffmpeg` and `ffprobe` are installed
- 💪 Auto-install `yt-dlp` if missing
- 📁 Save files to current script folder (for now)

---

## 📚 Requirements

- Python 3.7+
- yt-dlp (Auto-installed if missing)
- ffmpeg and ffprobe (For post-processing videos or extracting audio)

---

## ⚖️ How to Use

1. Make sure you have Python installed.
2. Install dependencies (if not auto-installed):
    ```bash
    pip install yt-dlp
    ```
3. Install FFmpeg:
    - Download from: [https://www.gyan.dev/ffmpeg/builds/](https://www.gyan.dev/ffmpeg/builds/)
    - Extract and add `/bin/` folder to your system PATH.
4. Run the script:
    ```bash
    python main.py
    ```
5. Paste your YouTube URL when asked.
6. Choose your preferred download option (Best Quality, Audio Only, 720p).

---

## 🛠️ Planned Future Features (Bonus Ideas)

- 📁 Allow users to **choose download folder** (e.g., Desktop, D:\Videos)
- 📅 Allow **renaming video** after download
- 🎵 **Select output audio format** (e.g., mp3, wav, aac)
- 📹 **Download full YouTube playlists**
- 📊 Show **live download speed** and **estimated time left**
- 📹 **Select specific resolution manually** (360p, 480p, 720p, 1080p)
- 📥 **Batch download** multiple URLs (copy-paste multiple links)
- 🎨 Build a simple **Graphical User Interface (GUI)** using `tkinter`
- 📦 **Bundle ffmpeg inside the .exe** for full portability

---

## 🚀 Credits

- Built with ❤️ using [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- Inspired by the idea of creating lightweight open-source utilities.

---

## 🎉 License

This project is licensed under the **MIT License**. Feel free to use and modify for personal or educational purposes.

