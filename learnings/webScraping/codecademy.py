import requests,sys,webbrowser,bs4

from selenium import webdriver

URL=raw_input('Enter URL \n')
browser=webdriver.Firefox()
browser.get(URL)

emailElem=browser.find_element_by_id('user_login')
emailElem.send_keys('konatalaramesh@gmail.com')

passwordElem=browser.find_element_by_id('user_password')
passwordElem.send_keys('')
passwordElem.submit()
currentUrl="https://www.codecademy.com/en/courses/web-ext/projects/html-css-prj_broadway"

browser.get(currentUrl)
res=requests.get(currentUrl)
res.raise_for_status()
print('Converting....')
soup=bs4.BeautifulSoup(res.text,"html.parser")
print soup
with open('C:\Users\konat\Desktop\oliveboard\learnings\webScraping\codecademy.html', 'w') as f:
   for line in soup.prettify('utf-8', 'minimal'):
      f.write(str(line))

