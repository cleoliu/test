#-*- coding: utf-8 -*-　　 
#-*- coding: cp950 -*-　
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
import time
import cv2



########## TEST ##########
def filesincowork(self):
        driver = self.driver
        url = linecache.getline('cmd.txt',1).rstrip('\n') 
        driver.get(url)
        
        # cowork icon
        sleep(10)
        driver.find_element_by_xpath("//article/div/i").click()
        
        # upload button
        sleep(10)
        driver.find_element_by_css_selector("a.work-tool-btn > i.icon-uploadfromdevice_01").click()
        
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
            driver.find_element_by_css_selector("div.file-top-panel.uk-panel > input[type=\"file\"]").send_keys(os.getcwd()+"/ppp2/"+file[star]) #upload file
            sleep(20)
            self.assertEqual(file[star], driver.find_element_by_xpath("//header/div[2]/h3").text) #assertEqual cowork file name
            sleep(5)
            count = len(driver.find_elements_by_xpath("/html/body/ui-view/ui-view/div[3]/u3d-work-viewer/section/section/div[4]/section/div[2]/u3d-tabs/div/div[2]/u3d-panel/div/u3d-chatroom/div[2]/div[1]/div/ul/li")) #count chatroom elements
            if linecache.getline('version.txt',1).rstrip('\n') == "1.23" :
                driver.find_element_by_id("chatroomTextarea").send_keys(Keys.ENTER) #chatroom page donw
                self.assertEqual(file[star], driver.find_element_by_xpath("//li["+str(count)+"]/u3d-chatroom-msg/div/section/div[2]/div/h6").text) #assertEqual chatroom file name
                sleep(5)
            else:
                pass
            
        #alert
        sleep(10)
        driver.get(url)
        sleep(10)
        alert = driver.switch_to_alert()
        alert.accept()    
        sleep(15)

        # open file
        star = 0
        for X in range(countlist):
            star += 1
            if star == 1:
                driver.find_element_by_xpath("//article/section/div").click() # open file
            else:
                driver.find_element_by_xpath("//u3d-scene-matter["+str(star)+"]/article/section/div").click() # open file
            sleep(25)
            newfile = file[::-1] #reverse file[list]
            picname = "Cowork_" + newfile[star-1] + ".jpg"
            driver.save_screenshot(os.path.join(path, picname))
            driver.find_element_by_css_selector("label.icon-close").click() # close file
            sleep(10)
            #pic cut
            img = cv2.imread(path+"/"+picname)
            height, width, channels = img.shape
            clp = img[height-1268:height-65, width-1660:width-530]    # up_height:down_height , left_width:right_width
            cv2.imwrite(os.path.join(path, picname), clp)
    
        # close cowork
        driver.find_element_by_xpath("//u3d-work-viewer/ul/li[3]/a/i").click()  

########## TEST END ##########

 
