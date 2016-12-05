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

########## TEST ##########
def minifycowork(self):
        driver = self.driver
        url = linecache.getline('cmd.txt',1).rstrip('\n') 
        driver.get(url)     
        #if last case fail alert accept
        sleep(10)
        try:
            alert = driver.switch_to_alert()
            alert.accept()
            sleep(10)
            driver.find_element_by_css_selector("a.work-btn > i.icon-close").click()  
        except:
            pass
        
        # open cowork
        sleep(20)
        driver.find_element_by_xpath("//article/div/i").click()
        #driver.find_element_by_xpath("/html/body/ui-view/ui-view/div[2]/div[4]/div[2]/div/div/div/article[1]/div[1]/i").click()

        # minify
        sleep(15)
        driver.find_element_by_css_selector("i.icon-minify").click()
        
        # right minify cowork icon
        sleep(20)
        try:
                driver.find_element_by_css_selector("li.task.ng-scope > article > div.ng-scope > i.matter-sprites.matter-work").click()
        except:
                driver.find_element_by_xpath("//li/article/div/i").click()

        # close
        sleep(10)
        driver.find_element_by_css_selector("a.work-btn > i.icon-close").click()
        
########## TEST END ##########