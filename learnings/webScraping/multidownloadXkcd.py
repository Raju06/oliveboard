#! python3
   # multidownloadXkcd.py - Downloads XKCD comics using multiple threads.
from __future__ import unicode_literals
import youtube_dl
import requests,sys,webbrowser,bs4,re
from pytube import YouTube

# not necessary, just for demo purposes.
from pprint import pprint
import requests, os, bs4, threading
 # store comics in ./xkcd

def main(item):
	ydl_opts = {}

	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
		ydl.download([item])


    #display text while downloading the Google page
def mainCode(numberStart,numberStop):
	for number in range(numberStart,numberStop):
		if number==0:
			k=''
		else:
			k=str('/&p={}'.format(number))
		item=str('http://www.xvideos.com/?k=indian+college{}'.format(k))
		print 'Downloading {}...'.format(str('http://www.xvideos.com/?k=indian+college{}'.format(k)))
		res=requests.get(item)
		res.raise_for_status()
		soup=bs4.BeautifulSoup(res.text,"html.parser")
		linkElems=soup.select('.mozaique a')
		print len(linkElems)
		URLlist=[]
		for i in range(len(linkElems)):
			URLlist.append(str('http://www.xvideos.com'+linkElems[i]['href']))
		for i in range(len(URLlist)):
			main(URLlist[i])
			print 'downloading ',URLlist[i]


def downloadXkcd(startComic, endComic):
  for urlNumber in range(startComic, endComic):
  # Download the page.
    print('Downloading page http://xkcd.com/%s...' % (urlNumber))
    res = requests.get('http://xkcd.com/%s' % (urlNumber))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text,"html.parser")
    # Find the URL of the comic image.
    comicElem = soup.select('#comic img')
    if comicElem == []:
      print('Could not find comic image.')
    else:
      comicUrl = 'http:'+comicElem[0].get('src')
      # Download the image.
      print('Downloading image %s...' % (comicUrl))
      res = requests.get(comicUrl)
      res.raise_for_status()
      # Save the image to ./xkcd.
      imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
      for chunk in res.iter_content(100000):
        imageFile.write(chunk)
      imageFile.close()

downloadThreads=[] # a list of all Thread objects
k=0
for number in range(0,10,2):
	
	downloadThread=threading.Thread(target=mainCode,args=(number,number+1))
	downloadThreads.append(downloadThread)
	downloadThread.start()

for downloadThread in downloadThreads:
    downloadThread.join()
print('Done.')
