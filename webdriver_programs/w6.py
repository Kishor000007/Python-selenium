#program to close all the window one after the other
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.lambdatest.com/selenium-playground/window-popup-modal-demo")
driver.maximize_window()
driver.find_element(By.ID,"followall").click()
time.sleep(20)
allwindows=driver.window_handles
print(allwindows)

for i in allwindows:
    driver.switch_to.window(i)
    driver.close()

time.sleep(10)