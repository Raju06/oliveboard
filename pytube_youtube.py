from pytube import YouTube
from os.path import realpath

# not necessary, just for demo purposes.
from pprint import pprint

yt = YouTube("https://www.youtube.com/watch?v=bM7SZ5SBzyY")

# Once set, you can see all the codec and quality options YouTube has made
# available for the perticular video by printing videos.

pprint(yt.get_videos())
print(yt.filename)
yt.set_filename(yt.filename)
video=yt.get('mp4','720p')
video.download(realpath(''))
