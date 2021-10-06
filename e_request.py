import requests
r = requests.get('https://api.github.com/events')
data = r.content
data2= r.text
print(type(data),type(data2))