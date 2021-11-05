# YouTube song/video downloader

import argparse
import sys, os
from pytube import YouTube, Stream
#from pytube.cli import on_progress

#TODO:
# 1. Make progress bar
# 2. Display the size of video file

"""
USAGE :
    * To download a song/video from YouTube 
      $ python3 ytd.py [Options] [-l] [yt-song-url]
    * Default location for downloaded file is in Music directory
    * You can change the location by giving the folder name
    * when prompted for folder location
"""

# HEX-COLORS
RED    = '\33[91m'
GREEN  = '\33[32m'
YELLOW = '\33[93m'
CYAN   = '\033[96m'
FAIL   = '\033[91m'
RST    = '\033[0m'  #reset

def get_video(ytv):
  print("Video Title: ", ytv.title)
  # progressive streams have the video and audio in a single file
  video_stream = ytv.streams.filter(progressive=True,
                                    file_extension='mp4',
                                    type='video')
  # store the available resolutions
  video_res = []
  for s in video_stream:
    video_res.append(s.resolution)
  video_res = list(set(video_res))
  print("Available Resolution :", end=" ")
  for vr in video_res:
    print(vr,end=", ")
  user_res = input("Choose the resolution: ")
  video_to_download = video_stream.filter(res=user_res).first()
  downloader(video_to_download, ytv.title)
  
def get_audio(yts):
  print("Song Title: ", yts.title)
  song_stream = yts.streams.filter(only_audio=True).first()
  size = round(song_stream.filesize_approx/1000000,3)
  print("Size: {} MB".format(size))

  #download audio/song
  downloader(song_stream, yts.title)

def downloader(strm, name):
  #ask user to proceed or not
  user_input = input("Do you want to download[y/N]: ")
  if user_input == "y":
    file_path = getpath()
    print(f"{RED} Downloading: {name}")
    strm.download(file_path)
    print(f"{GREEN} Finished Downloading: {name}")
  else:
    sys.exit()

def getpath():
  home = os.path.expanduser('~')
  default_path = 'Music'   #default folder
  user_path = input("Enter the directory[default: Music]: ")
  if user_path == '':
    user_path = default_path
  down_path = os.path.join(home, user_path)
  return down_path

def error_msg():
  print(f" {FAIL}ytd: Error occured !{RST}")
  print(" Possible reason: ")
  print("      * Connection is poor")
  print("      * Invalid URL ")
  print("--------- Try Again -----------")

def main():
  #create parser
  parser = argparse.ArgumentParser(description='ytd : a cli YouTube song/video downloader')
  parser.add_argument('-a','--audio',
                      action='store_true',
                      help='get the audio file')
  parser.add_argument('-v','--video',
                      action='store_true',
                      help='get the video file')
  parser.add_argument('--l',
                      type=str,
                      action='store',
                      help='YouTube url')
  parser.add_argument('--version',
                      action='version',
                      version='%(prog)s 1.2')
  # Parse the argument
  args = parser.parse_args()
  url  = args.l
  try:
    yt = YouTube(url)
  except:
    error_msg()
    sys.exit()

  if args.audio:
    get_audio(yt)
  elif args.video:
    get_video(yt)
  else:
    print(f"{FAIL}Error: invalid options")
    sys.exit()

main()
