from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
import linecache #cmd.txt
import os #os.getcwd()


########## TEST ##########
def publicchat(self):
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
        
        # cowork icon
        sleep(10)
        driver.find_element_by_xpath("//article/div/i").click()
        
        # public chat message 
        sleep(10)
        driver.find_element_by_id("chatroomTextarea").send_keys("hello selenium")
        driver.find_element_by_id("chatroomTextarea").send_keys(Keys.ENTER)
        
        # matter
        #sleep(10)
        #driver.find_element_by_xpath("//form/div[2]/button[2]").click() #+
        #sleep(10)
        #driver.find_element_by_css_selector("section.panel-box > input.file-select").send_keys(os.getcwd()+"/ppp2/ppt.ppt")
        #sleep(10)
        #driver.find_element_by_xpath("//div[3]/button[2]").click() #+
        #try:
         #   driver.find_element_by_xpath("//div/section[2]/ul/li[1]/button").click() #preview   #general v1.23 dont pre (but ctf uncerter rule , 1.23 need pre)
        #except:
         #   pass 
        
        # url
        sleep(15)
        driver.find_element_by_xpath("//form/div[2]/button[2]").click() #+
        sleep(15)
        driver.find_element_by_css_selector("div.chatroom-add-card-bar.ng-scope > u3d-add-card-bar.ng-isolate-scope > div.ng-scope > section.add-card-bar > section.panel-box > section.paste-link-box > span > input.input-path").send_keys("www.yahoo.com")
        sleep(15)
        try:
            driver.find_element_by_xpath("//form/div/u3d-add-card-bar/div/section/section[2]/section/span[2]/button").click() #perview button
            sleep(15)
            driver.find_element_by_xpath("//div/section[2]/ul/li[1]/button").click() #perview   #general v1.23 dont pre (but ctf uncerter rule , 1.23 need pre)
        except:
            pass 
            
        # matter from home
        sleep(15)
        driver.find_element_by_xpath("//form/div[2]/button[2]").click() #+
        sleep(15)
        driver.find_element_by_xpath("//section[2]/ul/li[3]/button").click() #from home change button
        sleep(15)
        driver.find_element_by_css_selector("div.home-matters-list > ul > li.ng-scope").click() #"test" folder
        sleep(15)
        driver.find_element_by_css_selector("span.home-matters-list-name.ng-binding").click() #ast.txt
        sleep(15)
        driver.find_element_by_xpath("//div[2]/div/button").click() #enter button
        sleep(15)
        try:
        	driver.find_element_by_xpath("//form/div[2]/button[3]").click() #back
        except:
            pass
        
        # recording
        sleep(15)
        driver.find_element_by_xpath("//form/div[2]/button[2]").click() #+
        sleep(15)
        driver.find_element_by_xpath("//li[4]/button").click() #recording button
        sleep(15)
        try:
        	driver.find_element_by_xpath("//li[5]/button").click() #end
        except:
            pass
        sleep(10)
        
        # close cowork
        driver.find_element_by_css_selector("a.work-btn > i.icon-close").click()  
        
########## TEST END ##########