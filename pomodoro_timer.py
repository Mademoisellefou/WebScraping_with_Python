import time
import  os
from selenium import  webdriver
class Pomodoro:
    def __init__(self):
        self.t=1
        self.c=1
        self.driver=driver
    def start(self,_time=10):
        self.t=_time*60
        while self.t:
            if(self.t%2==0):
                c+=1
                self.driver.get("https://inventwithpython.com/hacking/chapter{}.html".format(c))
            time.sleep(1)
            self.t-=1
        self.end("fin")
    def end(self,msg):
        print(msg)
    def __exit__(self,exc_type,exc_val,exc_tb):
        self.close()
        self.quit()
driver_path="/usr/bin/chromedriver"
os.environ['PATH']+=os.pathsep + driver_path
driver=webdriver.Chrome()        
p=Pomodoro(driver)
p.start(3)

