# requests a url  using requests
import requests
r = requests.get('https://api.github.com/events')
data = r.content
data2= r.text
print(type(data),type(data2))

# requests a url using selenium
from selenium import webdriver
import os
# path to ChromeDriver.exe
path = os.path.join('c:\\', 'Users\libia\Downloads\chromedriver\chromedriver.exe')
#creating a instance
driver=webdriver.Chrome(path)
url = 'https://www.foxnews.com/'
driver.get(url)

