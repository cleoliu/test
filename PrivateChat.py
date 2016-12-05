from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep
from selenium.webdriver import ActionChains
import linecache #cmd.txt
import os #os.getcwd()



########## TEST ##########
def privatechat(self):
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
        sleep(15)

        # choose friend
        try:
            # mouseover
            try:
            #avoid click myself
                element = driver.find_element_by_xpath("//li[3]/a[3]/h5")
            except:
                element = driver.find_element_by_xpath("//li[2]/a[3]/h5")
            hover = ActionChains(driver).move_to_element(element)
            hover.perform()
            sleep(15)
            driver.find_element_by_css_selector("div.active > i.icon-comment").click()
        except:
            sleep(10)
            driver.find_element_by_xpath("//li[2]/a[3]/h5").click() #ctf

        # message
        sleep(10)
        driver.find_element_by_xpath("//u3d-panel[2]/div/u3d-chatroom/div[2]/div[3]/form/div[2]/textarea").send_keys("hello selenium")
        driver.find_element_by_xpath("//u3d-panel[2]/div/u3d-chatroom/div[2]/div[3]/form/div[2]/textarea").send_keys(Keys.ENTER)
        sleep(10)
        
        # matter
        #driver.find_element_by_xpath("//u3d-panel[2]/div/u3d-chatroom/div[2]/div[3]/form/div[2]/button[2]").click() #+
        #sleep(5)
        #driver.find_element_by_css_selector("section.panel-box > input.file-select").send_keys(os.getcwd()+"/ppp2/ppt.ppt")
        #sleep(10) # waitting upload
        #driver.find_element_by_xpath("//div[3]/button[2]").click() #+
        #try:
         #   driver.find_element_by_xpath("//div/section[2]/ul/li/button").click() #preview  ######general v1.23 dont pre (but ctf uncerter rule , 1.23 need pre)
        #except:
         #   pass

        # url
        sleep(5)
        driver.find_element_by_xpath("//u3d-panel[2]/div/u3d-chatroom/div[2]/div[3]/form/div[2]/button[2]").click() #+
        driver.find_element_by_xpath("//form/div/u3d-add-card-bar/div/section/section[2]/section/span/input").send_keys("www.yahoo.com")
        sleep(5)
        try:
            driver.find_element_by_xpath("//form/div/u3d-add-card-bar/div/section/section[2]/section/span[2]/button").click() #perview button
            sleep(10)
            driver.find_element_by_xpath("//div/section[2]/ul/li[1]/button").click() #perview  ######general v1.23 dont pre (but ctf uncerter rule , 1.23 need pre)
        except:
            pass

        # matter from home
        sleep(5)
        driver.find_element_by_xpath("//u3d-panel[2]/div/u3d-chatroom/div[2]/div[3]/form/div[2]/button[2]").click() #+
        sleep(5)
        driver.find_element_by_xpath("//section[2]/ul/li[3]/button").click() #from home change button
        sleep(5)
        driver.find_element_by_css_selector("div.home-matters-list > ul > li.ng-scope").click() #"test" folder
        sleep(5)
        driver.find_element_by_css_selector("span.home-matters-list-name.ng-binding").click() #test folder
        sleep(5)
        driver.find_element_by_xpath("//div[2]/div/button").click() #enter button
        sleep(10)
        try:
        	driver.find_element_by_xpath("//u3d-panel[2]/div/u3d-chatroom/div[2]/div[3]/form/div[2]/button[3]").click() #back
        except:
        	pass
       
        # recording
        sleep(5)
        driver.find_element_by_xpath("//u3d-panel[2]/div/u3d-chatroom/div[2]/div[3]/form/div[2]/button[2]").click() #+
        sleep(5)
        driver.find_element_by_xpath("//li[4]/button").click() #recording button
        sleep(5)
        try:
        	driver.find_element_by_xpath("//li[5]/button").click() #end
        except:
            pass
        sleep(10)
        
        # close cowork
        driver.find_element_by_css_selector("a.work-btn > i.icon-close").click()  

########## TEST END ##########