from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import linecache
import os #os.getcwd()

########## TEST ##########
def invite4contactsintocowork(self):
        driver = self.driver
        url = linecache.getline('cmd.txt',1).rstrip('\n') 
        driver.get(url)
        
        # cowork
        sleep(10)
        driver.find_element_by_css_selector("i.icon-add_work").click()
        sleep(5)
        DATE = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        driver.find_element_by_name("work[title]").send_keys("selenium cowork_"+DATE)
        sleep(5)
        driver.find_element_by_css_selector("div.cover-picture > input.file-select").send_keys(os.getcwd()+"/ppp2/pika.jpg")
        sleep(10)
        driver.find_element_by_xpath("//div[3]/input").click()
        sleep(15)
        driver.find_element_by_css_selector("ul.actions.ng-scope > li > i.icon-friend_add").click()
        sleep(5)
        driver.find_element_by_xpath("//div[@id='contact-scroll']/ul/li[1]/h5").click()
        sleep(5)
        driver.find_element_by_xpath("//div[@id='contact-scroll']/ul/li[2]/h5").click()
        sleep(5)
        driver.find_element_by_xpath("//div[@id='contact-scroll']/ul/li[3]/h5").click()
        sleep(5)
        driver.find_element_by_xpath("//div[@id='contact-scroll']/ul/li[4]/h5").click()
        sleep(5)
        driver.find_element_by_xpath("//footer/ul/li/button").click()
        sleep(5)
        driver.find_element_by_xpath("//footer/ul/li/button").click()
        sleep(5)
        
        #close cowork
        driver.find_element_by_xpath("//u3d-work-viewer/ul/li[3]/a/i").click() 
########## TEST END ##########