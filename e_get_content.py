import requests
from bs4 import BeautifulSoup
r = requests.get('https://api.github.com/events')
data = r.content
data2= r.text
print(type(data),type(data2))

soup = BeautifulSoup(data2, "html.parser")