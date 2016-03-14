from selenium import webdriver
browser=webdriver.Firefox()
browser.get('http://youtube.com')
linkElem=browser.find_element_by_link_text('Trending')
type(linkElem)
linkElem.click()