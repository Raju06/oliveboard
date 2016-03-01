import urllib2
from collections import Counter

url = 'https://en.wikipedia.org/wiki/Israel'

response = urllib2.urlopen(url)
webContent = response.read()

a= webContent.split()


input =  a
c = Counter( input )

k=c.items() 

k.sort(key=lambda x: x[1])
print k[len(k)-100:len(k)-30]