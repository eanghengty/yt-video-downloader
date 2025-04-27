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

# 📌 main function to download the video
def download_video():
    url = input("Enter the url: ")


    yt_opts={} # you can add option here like quality
    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download([url])
# start the program
if __name__ == "__main__":
    download_video()