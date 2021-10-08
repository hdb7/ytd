# YouTube song downloader

import sys, os
from pytube import YouTube, Stream
#from pytube.cli import on_progress

#TODO:
# 1. Make progress bar

"""
USAGE :
    * To download a song from YouTube 
      $ python3 ytd.py <yt-song-url>
    * Default location for downloaded file is in Music directory
    * You can change the location by giving the folder name
    * when prompted for folder location
"""

# HEX-COLORS
RED    = '\33[91m'
GREEN  = '\33[32m'
YELLOW = '\33[93m'
CYAN = '\033[96m'
FAIL = '\033[91m'
RST = '\033[0m'  #reset


def help():
  print("ytd 1.0, a cli YouTube song downloader")
  print(" Usage: ")
  print("   ytd [Option] [Url]")
  print(" Option: ")
  print("   -h     display this help")

def download_path():
  home = os.path.expanduser('~')
  default_path = 'Music'   #default folder
  user_path = input("Enter the directory[default: Music]: ")
  if user_path == '':
    user_path = default_path
  down_path = os.path.join(home, user_path)
  return down_path

def main():
  arg = sys.argv[1]
  if arg == "-h":
    help()
    sys.exit()
  else:
    url = arg
  try:
    yts = YouTube(url)
  except:
    print(f" {FAIL}ytd: Sorry :( Unable to fetched the content ! {RST}")
    print(" Possible reason: \n * your offline \n * invalid url\n\n  Try again.")
    sys.exit()

  print("Song Title: ", yts.title)
  song_stream = yts.streams.filter(only_audio=True).first()

  #global size  #make it accessible
  size = round(song_stream.filesize_approx/1000000,3)
  print("Size: {} MB".format(size))

  #ask user to proceed or not
  user_input = input("Do you want to download[y/N]:")
  if user_input == "y":
    file_path = download_path()
    print(f"{RED} Downloading: {yts.title}")
    song_stream.download(file_path)
    print(f"{GREEN} Finished Downloading: {yts.title}")
  else:
    sys.exit()

main()
