import requests,sys,webbrowser,bs4,re
from pytube import YouTube

# not necessary, just for demo purposes.
from pprint import pprint


    #display text while downloading the Google page
res=requests.get('https://www.youtube.com/playlist?list=PLvFYFNbi-IBFeP5ALr50hoOmKiYRMvzUq')
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,"html.parser")

with open('C:\Users\Olive\Desktop\oliveboard\learnings\webScraping\prettifyHTML.txt', 'w') as f:
   for line in soup.prettify('utf-8', 'minimal'):
      f.write(str(line))

linkElems=soup.select('.pl-video-title-link')
for i in range(1):	
	#https://www.youtube.com/watch?v=Sqitl2Rlsis&list=PLSSPBo7OVSZszs6coWD3nnAhJyVe_2drG&index=45
	Url=str('https://www.youtube.com')+linkElems[i]['href']
	print('Downloading file no. {} ....').format(i+1)
	yt = YouTube(Url)
	yt.set_filename(yt.filename)
	video=yt.get('mp4','360p')
	video.download('C:\Users\Olive\Desktop')
	print "Downloaded file"