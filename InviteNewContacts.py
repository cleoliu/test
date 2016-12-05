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
def invitenewcontacts(self):
        driver = self.driver
        url = linecache.getline('cmd.txt',1).rstrip('\n') 
        driver.get(url)
        sleep(10)
        # RandomEmail
        mail_list = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']
        mail = "".join(sample(mail_list, 8)).replace(' ', '')
        
        
        # invite friend
        driver.find_element_by_css_selector("i.icon-friend_add").click()
        sleep(10)
        driver.find_element_by_name("contact[email]").send_keys(mail, "@yopmail.com")
        sleep(10)
        driver.find_element_by_css_selector("input[type=\"submit\"]").click()
########## TEST END ##########