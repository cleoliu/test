from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from random import randrange, sample
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import linecache

  
########## TEST ##########
def cloudbook(self):
        driver = self.driver
        url = linecache.getline('cmd.txt',1) .rstrip('\n')
        driver.get(url)
        
        #cloudbook
        sleep(15)
        driver.find_element_by_xpath("//div[3]/div/ul/li[5]/a/i").click()
        sleep(10)
        DATE = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        driver.find_element_by_name("catalog[title]").send_keys("selenium cloudBook_"+DATE)
        sleep(10)
        driver.find_element_by_xpath("//div[3]/input").click() # www
        sleep(12) 
        driver.find_element_by_xpath("//li[3]/div/ul/li[4]/a").click() #X
        
########## TEST END ##########