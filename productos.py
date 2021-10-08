# Encontrar los productos 

from bs4 import BeautifulSoup
import requests
import re
url ="https://www.ketal.com.bo"
page=requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")
content_titles=soup.find_all('div',class_="subitem")
links =[]
for i in content_titles:
    for j in i.find_all('a'):
        links.append(j.get('href'))
print("like :{}  total :{}".format(links[0],len(links)))      
