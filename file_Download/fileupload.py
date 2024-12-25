#In python, we upload file by using send_keys() by providing path into it....

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ser_obj=Service("D:/python_selenium/pythonProject/drivers/chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a").click()
driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[1]/header/div[2]/nav/ul/li[3]").click()
upload=driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[1]/div[1]/div/div[2]/div/button")
upload.send_keys(r"C:\Users\kisho\1707119468910.jpg")
time.sleep(5)