# 📌 check and install whether yt-dl install or not yet
try:
    import yt_dlp
except ModuleNotFoundError:
    import subprocess
    import sys
    print("📦 yt-dlp not found, installing...")
    subprocess.check_call([sys.executable
                           ,"-m","pip","install","yt-dlp"])
    import yt_dlp #try again after install
import shutil
import os

# 📌 check if ffmpeg install
def find_ffmpeg_folder():
    ffmpeg_path=shutil.which("ffmpeg")
    ffprobe_path=shutil.which("ffprobe")
    if ffmpeg_path and ffprobe_path:
        # ✅ Return folder path, not file path
        return os.path.dirname(ffmpeg_path)
    else:
        print("⚠️ Ffmpeg not found! please install it to get the best quality download.")
        print("You can download it here: https://www.gyan.dev/ffmpeg/builds/")
        return None
        

# 📌 main function to download the video
def download_video():
    url = input("Enter the url: ")

    ffmpeg_folder=find_ffmpeg_folder() # 📌 Detect ffmpeg path automatically

    print("\nChoose quality:")
    print("1. Best quality (default)")
    print("2. audio only (mp3)")
    print("3. 720p if available")
    choice = input("Enter your choice (1/2/3): ")

# 📌 setting options best on user choice
    if choice == "2":
        yt_opts={

            'format': 'bestaudio/best',
            'postprocessors':[{
                'key':'FFmpegExtractAudio',
                'preferredcodec':'mp3',
                'preferredquality':'192',
            }],
            'outtmpl':'%(title)s.%(ext)s',
            
        }
    elif choice =="3":

        yt_opts={
            'format':'bestvideo[height<=720]+bestaudio/best[height<=720]',
            'outtmpl':'%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            
        }
    else: # default best quality it can get
        yt_opts={
            'format':'bestvideo+bestaudio/best',
            'outtmpl':'%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
            

        }

    # 📌 If ffmpeg is found, tell yt-dlp where it is
    if ffmpeg_folder:
        yt_opts['ffmpeg_location'] = ffmpeg_folder
    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download([url])
# start the program
if __name__ == "__main__":
    download_video()