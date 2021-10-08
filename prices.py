#Conseguir los precios
from bs4 import BeautifulSoup
import requests
import re

#url =links[1]
url="https://www.ketal.com.bo/leches-en-polvo-formulas"
page=requests.get(url)
soup=BeautifulSoup(page.content,"html.parser")

content_titles=soup.find_all('div',class_="product-thumb")
products ={}
for i in content_titles:
    info=i.find_all('div',class_="caption")
    for detail in info:
        price=str(detail.find_all('div',class_="price"))
        price=re.findall(r'"price-normal">(.*?)</span>',price)
        name=str(detail.find_all('div',class_="name"))
        name=re.findall(r'limit=24">(.*?)</a>',name)
        print(name[0],price[0])
