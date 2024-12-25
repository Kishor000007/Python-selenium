import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ser_obj=Service("D:/python_selenium/pythonProject/drivers/chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://app.elorus.com/login/")
resetpwd=driver.find_element(By.XPATH,"//a[text()='Reset password.']")

action=ActionChains(driver)
action.context_click(resetpwd).perform()
time.sleep(2)