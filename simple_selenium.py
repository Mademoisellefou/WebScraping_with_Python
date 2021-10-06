from selenium import  webdriver
import  os
#
User=str(input('>Username '))
#
Password=str(input('>Password '))
nro=int(input('>nro '))
driver_path="/usr/bin/chromedriver"
os.environ['PATH']+=os.pathsep + driver_path
driver=webdriver.Chrome()
driver.get('http://{}:{}@natas{}.natas.labs.overthewire.org'.format(User,Password,nro))
