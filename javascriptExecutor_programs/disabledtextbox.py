import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser_obj=Service("D:/python_selenium/pythonProject/drivers/chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("file:///C:/Users/kisho/OneDrive/Attachments/Desktop/selenium7.html")
driver.execute_script("document.getElementById('i1').value='Selenium'")
time.sleep(3)