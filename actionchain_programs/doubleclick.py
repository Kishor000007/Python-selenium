import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ser_obj=Service("D:/python_selenium/pythonProject/drivers/chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("file:///C:/Users/kisho/OneDrive/Attachments/Desktop/doubleclick.html")
button=driver.find_element(By.XPATH,"//button[text()='Double-click me']")

action=ActionChains(driver)
action.double_click(button).perform()
time.sleep(3)