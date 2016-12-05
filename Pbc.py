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
import csv
import os #os.getcwd()

#alpha


def pbc(self):
        driver = self.driver
        url = linecache.getline('cmd.txt',1).rstrip('\n') 
        driver.get(url)
        sleep(10)
        # DATE
        DATE = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        # RandomEmail
        mail_list = ['z','y','x','w','v','u','t','s','r','q','p','o','n','m','l','k','j','i','h','g','f','e','d','c','b','a']
        mail_adduser = "".join(sample(mail_list, 8)).replace(' ', '')
        mail_csv = "".join(sample(mail_list, 8)).replace(' ', '')
        # csv
        headers = ['employee_id','email','first_name','last_name','social_id','gender','birthday','on_board','department_id','title','contactor','contactor_phone','contactor_mobile','education','graducation','address_1','address_2','remark','groups','roles']
        rows = ["",mail_csv+"@picowork.com","Selenium_","ImportCsv","","male"]
        f =  open('stocks.csv','wb')
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerow(rows)
        f.close()
        
        
        # click PBC icon
        try:
            driver.find_element_by_xpath("/html/body/ui-view/ui-view/div[2]/div[2]/div[3]/div/div/ul/li[2]/a/i").click()
        except:
            driver.find_element_by_xpath("/html/body/ui-view/ui-view/div[2]/div[3]/div/div/ul/li/a/i").click()
        try:
            driver.switch_to_frame(1)
        except:
            driver.switch_to_frame(2)

        sleep(5)
        
        # build account
        driver.find_element_by_xpath("/html/body/div/div/div/a[1]").click()
        driver.find_element_by_id("account_first_name").send_keys("Selenium")
        driver.find_element_by_id("account_last_name").send_keys("NewAccount")
        build_account = mail_adduser+"@picowork.com"
        driver.find_element_by_id("account_email").send_keys(build_account)
        driver.find_element_by_name("commit").click()
        sleep(5)

        
        # build group
        driver.find_element_by_xpath("/html/body/div/div/div/a[3]").click()
        sleep(5)
        driver.find_element_by_xpath("/html/body/div/div/div/a[1]").click()
        driver.find_element_by_id("group_name").send_keys("Selenium_"+DATE+"\n")
        driver.find_element_by_xpath("/html/body/div/div[2]/div/a[2]").click()
        sleep(5)


        # web upload csv
        driver.find_element_by_xpath("/html/body/div/div/div/a[2]").click()
        driver.find_element_by_css_selector("#file_upload").send_keys(os.getcwd()+"/stocks.csv")
        driver.find_element_by_xpath("//span/input[2]").click()
        driver.find_element_by_xpath("//body/div/div/a").click()
        sleep(5)

        
        # blockade user
        driver.find_element_by_id("search").send_keys(build_account+"\n")
        driver.find_element_by_xpath("//td[7]/a[2]").click()
        sleep(5)
        alert = driver.switch_to_alert()
        alert.accept()