from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
from selenium.webdriver.chrome.options import Options
import linecache


def login(self):
        driver = self.driver
        url = linecache.getline('cmd.txt',1).rstrip('\n') 
        user = linecache.getline('cmd.txt',2).rstrip('\n') 
        password = linecache.getline('cmd.txt',3).rstrip('\n') 

        driver.get(url)
        sleep(25)
        driver.find_element_by_name("user[email]").send_keys(user)
        driver.find_element_by_name("user[password]").send_keys(password)
        sleep(10)
        try:
            driver.find_element_by_xpath("(//button[@type='submit'])").click() # www
        except:
            driver.find_element_by_xpath("(//button[@type='submit'])[3]").click() # so-net
        sleep(20)
        
        # version
        driver.find_element_by_css_selector("i.irregular-spirtes.picowork-logo").click()
        version = driver.find_element_by_css_selector("div.row > i").text
        driver.find_element_by_css_selector("button.action-enter").click()
        f = open('version.txt', 'w')   
        f.write(version[0:4])
        f.close()
        
def ppp(self):
    
    print hihihi
