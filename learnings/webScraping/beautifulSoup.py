from bs4 import BeautifulSoup
import json
import urllib
r=urllib.urlopen('https://iimcat.ac.in/per/g01/pub/756/ASM/WebPortal/1/index.html?756@@1@@1').read()
soup=BeautifulSoup(r,'lxml')
letters=soup.find_all('section',class_="home-content")
print letters
lobbying={}
for element in letters:
	print element.a.get_text()
	lobbying[element.a.get_text()]={}
for element in letters:
	lobbying[element.a.get_text()]=element.a['href']
for item in lobbying.keys():
	print item + ": " +"\n\t"+"link: "+lobbying[item]+"\n\n"
