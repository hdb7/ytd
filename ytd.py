# YouTube song downloader

import sys, os
from pytube import YouTube, Stream

#TODO:
# 1. Make progress bar

def download_path():
  home = os.path.expanduser('~')
  user_path = 'Music'
  user_path = input("Enter the directory[default: Music]: ")
  down_path = os.path.join(home, user_path)
  return down_path

def download():
  link = sys.argv[1]
  yts = YouTube(link)
  print("Song Title: ", yts.title)
  song_stream = yts.streams.filter(only_audio=True).first()

  global size  #make it accessible
  size = round(song_stream.filesize_approx/1000000,3)
  print("Size: {} MB".format(size))

  #ask user to proceed or not
  user_input = input("Do you want to install[y/N]:")
  if user_input == "y":
    song_stream.download(download_path())
  else:
    sys.exit()

download()
