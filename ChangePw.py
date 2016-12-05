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


########## TEST ##########
def changepw(self):
        driver = self.driver
        url = linecache.getline('cmd.txt',1).rstrip('\n') 
        password = linecache.getline('cmd.txt',3).rstrip('\n') 
        driver.get(url)

        sleep(10)
        driver.find_element_by_css_selector("i.matter-sprite.matter-service-manager").click()
        sleep(5)
        driver.find_element_by_xpath("//li/div/div/div[2]/div/div/ul/li[2]").click()
        sleep(5)
        driver.find_element_by_xpath("//div[2]/div/ul/li[4]").click()
        sleep(5)
        driver.find_element_by_name("user[password]").send_keys(password)
        driver.find_element_by_name("user[password_confirmation]").send_keys(password)
        sleep(5)
        driver.find_element_by_xpath("//button[@type='submit']").click()
########## TEST END ##########