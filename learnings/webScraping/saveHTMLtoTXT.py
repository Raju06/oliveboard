import requests,sys,webbrowser,bs4,os


def main(URL):
	URL=str(URL)
	fileName=URL[53:len(URL)-11]
	print('Converting....  {}').format(fileName)
	wget ‐‐page-requisites ‐‐span-hosts ‐‐convert-links ‐‐adjust-extension http://example.com/dir/file
	location='C:\Users\konat\Desktop\codecademy\HTML_CSS\{}.html'.format(fileName)
	with open(location, 'w') as f:
	   for line in soup.prettify('utf-8', 'minimal'):
	      f.write(str(line))

main('https://s3.amazonaws.com/codecademy-content/projects/armando-perez/index.html')