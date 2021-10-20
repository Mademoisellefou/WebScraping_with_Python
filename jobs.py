import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
def extract(page):
    url= f"https://www.indeed.com/jobs?q=java&l=Miami%2C+FL&start={page}"
    headers={'User-Agent':"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"}
    r=requests.get(url,headers=headers)
    soup=BeautifulSoup(r.content,'html.parser')
    return soup
def transform(soup):
    divs=soup.find_all('div',class_='slider_container')
    for i in divs:
        title=i.find('h2')
        title=title.find('span').text.strip()
        company=i.find('span',class_='companyName')
        company=company.text.strip()
        job={
            'title':title,
            'company':company
        }
        listjobs.append(job)
    return listjobs
listjobs=[]
for i in range(0,30,10):    
    c=extract(i)
    transform(c)
df=pd.DataFrame(listjobs)
print(df.head())
df.to_csv('jobs.csv')
