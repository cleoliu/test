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
import sys
import cv2



########## TEST ##########
def filesindesk(self):
        driver = self.driver
        url = linecache.getline('cmd.txt',1).rstrip('\n') 
        driver.get(url)
        
        # upload button
        sleep(10)
        driver.find_element_by_css_selector("i.icon-uploadfromdevice_01").click()
        
        # mkdir folder
        path = os.getcwd()+"/PIC/"+url[8:]+time.strftime("_%Y-%m-%d")
        if not os.path.isdir(path):
            os.makedirs(path)        

        # upload file 12
        file = ["png.png", "pdf.pdf", "xls.xlsx", "mp3.mp3", "mp4.mp4", "zip.zip"]        
        countlist = len(file)
        star = -1
        for X in range(countlist):
            star += 1
            driver.find_element_by_css_selector("div.file-top-panel.uk-panel > input[type=\"file\"]").send_keys(os.getcwd()+"/ppp2/"+file[star])
            sleep(20) # wait upload
        
        # get url    
        driver.get(url)
        sleep(15)
        
        #open file    
        star = 0
        for X in range(countlist):
            star += 1
            if star == 1:
                driver.find_element_by_xpath("//article/div/i").click() # open file
            else:
                driver.find_element_by_xpath("//article["+str(star)+"]/div/i").click() # open file
            sleep(20)
            newfile = file[::-1] #reverse file[list]
            picname = "Desk_" + newfile[star-1] + ".jpg"
            driver.save_screenshot(os.path.join(path, picname))
            driver.find_element_by_css_selector("label.icon-close").click() # close file
            sleep(15)
            #pic cut     
            img = cv2.imread(path+"/"+picname)
            height, width, channels = img.shape
            clp = img[height-1318:height-45, width-1935:width-73]    # up_height:down_height , left_width:right_width
            cv2.imwrite(os.path.join(path, picname), clp)
            
        f = os.popen ("PicOpenCV.py",'r')
        print f.read()
            
            
########## TEST END ##########