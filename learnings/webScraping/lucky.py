import requests,sys,webbrowser,bs4

print('Googling....')    #display text while downloading the Google page
res=requests.get('https://www.google.co.in/webhp?sourceid=chrome-instant&ion=1&espv=2&ie=UTF-8#q='+' '.join(sys.argv[1:]))
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,"html.parser")
linkElems=soup.select('.r a')
print linkElems
numOpen=min(5,len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com'+linkElems[i].get('href'))
