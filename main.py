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
            'outtmpl':'%(title)s.%(ext)s'
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

    yt_opts={} # you can add option here like quality
    with yt_dlp.YoutubeDL(yt_opts) as ydl:
        ydl.download([url])
# start the program
if __name__ == "__main__":
    download_video()