import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ser_obj=Service("D:/python_selenium/pythonProject/drivers/chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://practice.expandtesting.com/drag-and-drop")
blockA=driver.find_element(By.ID,"column-a")
blockB=driver.find_element(By.ID,"column-b")

action=ActionChains(driver)
action.drag_and_drop(blockA,blockB).perform()
time.sleep(3)