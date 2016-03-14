import requests,sys,webbrowser,bs4

print('Googling....')    #display text while downloading the Google page
res=requests.get('https://www.google.co.in/search?q='+' '.join(sys.argv[1:]))
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,"html.parser")

with open('C:\Users\Olive\Desktop\oliveboard\learnings\webScraping\prettifyHTML.txt', 'w') as f:
   for line in soup.prettify('utf-8', 'minimal'):
      f.write(str(line))

linkElems=soup.select('.r a')
print linkElems
numOpen=min(5,len(linkElems))
for i in range(numOpen):
	webbrowser.open('http://google.com'+linkElems[i].get('href'))
