# YouTube song downloader

import sys, os
from pytube import YouTube, Stream
#from pytube.cli import on_progress

#TODO:
# 1. Make progress bar

# HEX-COLORS
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'

def download_path():
  home = os.path.expanduser('~')
  default_path = 'Music'   #default folder
  user_path = input("Enter the directory[default: Music]: ")
  if user_path == '':
    user_path = default_path
  down_path = os.path.join(home, user_path)
  return down_path

def download():
  link = sys.argv[1]

  try:
    yts = YouTube(link)
  except:
    print(f" {FAIL}ytd: Sorry :( Unable to fetched the content ! {ENDC}")
    print(" Possible reason: \n * your offline \n * invalid url\n\n  Try again.")
    sys.exit()

  print("Song Title: ", yts.title)
  song_stream = yts.streams.filter(only_audio=True).first()

  #global size  #make it accessible
  size = round(song_stream.filesize_approx/1000000,3)
  print("Size: {} MB".format(size))

  #ask user to proceed or not
  user_input = input("Do you want to install[y/N]:")
  if user_input == "y":
    file_path = download_path()
    print(f"{OKBLUE} Downloading: {yts.title} {ENDC}")
    song_stream.download(file_path)
    print(f"{OKGREEN} Finished Downloading: {yts.title} {ENDC}")
  else:
    sys.exit()

download()
