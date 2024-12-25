#program for current_window_handle,window_handles
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.lambdatest.com/selenium-playground/window-popup-modal-demo")
driver.maximize_window()
driver.find_element(By.ID,"followall").click()
time.sleep(20)
mainwindow=driver.current_window_handle
print(mainwindow)
allwindows=driver.window_handles
print(allwindows)

print(allwindows.__class__.__name__)

for i in allwindows:
    print(i)