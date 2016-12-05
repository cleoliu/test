# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from time import sleep
from selenium.webdriver import ActionChains

    
def deldeskfile(self):
        driver = self.driver
        sleep(10)
        
        # DEL FILE
        count = len(driver.find_elements_by_xpath("/html/body/ui-view/ui-view/div[2]/div[4]/div[2]/div/div/div/article"))
        star = 0
        for X in range(count-1):
            star += 1
            element = driver.find_element_by_xpath("//article["+str(star)+"]/div/i")
            hover = ActionChains(driver).move_to_element(element)
            hover.perform()
            driver.find_element_by_xpath("//article["+str(star)+"]/input").click()
        driver.find_element_by_xpath("//ul[2]/li[3]/a/i").click()
        


