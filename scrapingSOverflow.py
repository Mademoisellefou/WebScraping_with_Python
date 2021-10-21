import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
def extract():
    url= f"https://es.stackoverflow.com/questions?tab=Frequent"
    headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.content,'html.parser')
    return soup
def transform(soup):
    divs=soup.find_all('div',class_='question-summary')
    for i in divs:
        ctitle=i.find('div',class_='summary')
        title=ctitle.find('h3')
        title=title.find('a').text.strip()

        cvotos=i.find('div',class_='statscontainer')
        cvotos=cvotos.find('span',class_='vote-count-post')
        votos=cvotos.text.strip()

        rate ={
            'title':title,
            'voto':votos
        }
        ratings.append(rate)
ratings=[]
c=extract()
transform(c)
df=pd.DataFrame(ratings)
print(df.head())
df.to_csv('comments.csv',encoding='utf-8-sig')
