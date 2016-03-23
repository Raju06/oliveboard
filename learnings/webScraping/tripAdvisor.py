import urllib2
import json
import re
from bs4 import BeautifulSoup
 
url=raw_input("Enter Web URL :")
text = urllib2.urlopen(url).read()

for i in range(len(text)):
	if text[i:i+16] == "&maptype=roadmap":
		latitude,longitude=text[i-20:i].split(',')
		print "Latitude is {}".format(latitude)
		print "Longitude is {}".format(longitude)