from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest, time, re
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_cap = {'browser': 'Chrome', 'browser_version': '51.0', 'os': 'Windows', 'os_version': '7', 'resolution': '1024x768'}
app_url = "https://u3d.picowork.com/"

driver = webdriver.Remote(
    command_executor = 'http://udadmin:2JGJesQsQ9n9bEeRz84R@hub.browserstack.com:80/wd/hub',
    desired_capabilities = desired_cap)
driver.get(app_url)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "user[email]")))
driver.find_element_by_name("user[email]").clear()
driver.find_element_by_name("user[email]").send_keys("josh5@mailinator.com")
driver.find_element_by_name("user[password]").clear()
driver.find_element_by_name("user[password]").send_keys("bobobo")
driver.find_element_by_xpath("(//button[@type='submit'])").click()

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "roof"))).size() > 0

