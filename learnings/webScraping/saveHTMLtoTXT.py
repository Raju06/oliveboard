import requests,sys,webbrowser,bs4

URL=raw_input('Enter URL \n')
res=requests.get(str(URL))
res.raise_for_status()

print('Converting....')
soup=bs4.BeautifulSoup(res.text,"html.parser")

with open('C:\Users\Olive\Desktop\oliveboard\learnings\webScraping\saveHTMLtoTXT.html', 'w') as f:
   for line in soup.prettify('utf-8', 'minimal'):
      f.write(str(line))