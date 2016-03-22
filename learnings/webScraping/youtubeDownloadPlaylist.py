import requests,sys,webbrowser,bs4,re
from pytube import YouTube

# not necessary, just for demo purposes.
from pprint import pprint


    #display text while downloading the Google page
res=requests.get('https://www.youtube.com/watch?v=oT1A1KKf0SI&list=PLxxA5z-8B2xk4szCgFmgonNcCboyNneMD')
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,"html.parser")



linkElems=soup.select('.yt-uix-scroller-scroll-unit a')
print "Downloading {} videos\n\n".format(len(linkElems))
for i in range(len(linkElems)):	
	#https://www.youtube.com/watch?v=Sqitl2Rlsis&list=PLSSPBo7OVSZszs6coWD3nnAhJyVe_2drG&index=45
	try:	
		Url=str('https://www.youtube.com')+linkElems[i]['href']
		yt = YouTube(Url)
		print('Downloading file "{}" ....').format(yt.filename)
		yt.set_filename(yt.filename)
		video=yt.get('mp4','720p')
		video.download('C:\Users\konat\Desktop\Django')
		print "Downloaded file"
	except:
		print "Error downloading file...\ncontinuing download to next file"