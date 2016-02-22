import requests

url="https://en.wikipedia.org/wiki/Beautiful_Soup"
response=requests.get(url)
html=response.content
print html