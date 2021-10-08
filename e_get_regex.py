import requests
import re
r = requests.get('https://api.github.com/events')
data= r.text
ids = re.findall(r'"id":([0-9]*)', data)
idsres= [str(i) for i in ids]
print(idsres)
