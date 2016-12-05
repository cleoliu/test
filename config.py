#-*- coding: utf-8 -*-�@�@ 
import sys
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
import os
import logging

#import Login
from Login import *
from Cloudbook import *
from Invite4ContactsIntoCowork import *
from PrivateChat import *
from PublicChat import *
from FilesInCowork import *
from MinifyCowork import *
from FilesInDesk import *
from InviteNewContacts import *
from ChangePw import *
from Pbc import *
from DelDeskFile import *

class config(unittest.TestCase):
    def setUp(self):
        Tbrowser = linecache.getline('cmd.txt',4).rstrip('\n')
        Tbrowser_version = linecache.getline('cmd.txt',5).rstrip('\n')
        Tuser = linecache.getline('cmd.txt',6).rstrip('\n')

        
        ######## USE BROWSERSTACK ######## ----https://www.browserstack.com/automate/python
        desired_cap = {'browser': Tbrowser, 'browser_version': Tbrowser_version, 'os': 'Windows', 'os_version': '7', 'resolution': '2048x1536'}
        self.driver = webdriver.Remote(command_executor=Tuser,desired_capabilities=desired_cap)
        try:
            self.driver.set_window_size(2000,1500)
        except:
            pass

        
        ########## USA LOCAL PC ##########
        #self.driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe", service_args=["--verbose", "--log-path=D:\\qc1.log","--use-fake-ui-for-media-stream"])
        #self.driver.implicitly_wait(30)
        #self.verificationErrors = []
        #self.accept_next_alert = True
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      


    def test_1(self):
        try:
            print login(self)
            print '>>>>>Test_login(self) : PASS'
        except:
            print '>>>>>Test_login(self) : Fail'
        ############### CHOOSE TESTCASE ################
        lines = len(open("cmd.txt").readlines())-6
        case = 6
        for X in range(lines):
            case += 1
            try:
                str1 = linecache.getline('cmd.txt',case).rstrip('\n')
                exec str1
                print str1
                print '>>>>>Test_'+str1+' : PASS'
            except:
                print '>>>>>Test_'+str1+' : Fail'
                pass
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()