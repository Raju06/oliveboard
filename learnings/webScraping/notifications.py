import requests,sys,webbrowser,bs4

URL="https://iimcat.ac.in/per/g01/pub/756/ASM/WebPortal/1/index.html?756@@1@@1"
res=requests.get(str(URL))
res.raise_for_status()
soup=bs4.BeautifulSoup(res.text,"html.parser")

for each_div in soup.findAll('section',{'class':'home-content'}):
    print each_div