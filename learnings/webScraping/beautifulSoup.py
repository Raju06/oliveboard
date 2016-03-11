import requests,bs4
res=requests.get('http://nostarch.com')
res.raise_for_status()
noStarchSoup=bs4.BeautifulSoup(res.text,"html.parser")
type(noStarchSoup)

exampleFile=open('C:\Users\Olive\Desktop\oliveboard\learnings\webScraping\example.html')
exampleSoup=bs4.BeautifulSoup(exampleFile.read())
elems=exampleSoup.select('#author')
type(elems)
len(elems)
type(elems[0])
elems[0].getText()
str(elems[0])
elems[0].attrs