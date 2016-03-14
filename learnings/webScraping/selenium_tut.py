from selenium import webdriver
browser=webdriver.Firefox()
browser.get('http://accounts.google.com')
emailElem=browser.find_element_by_id('Email')
emailElem.send_keys('konatalaramesh@gmail.com')
emailElem.submit()
passwordElem=browser.find_element_by_id('Passwd-hidden')
passwordElem.submit()