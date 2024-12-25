import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ser_obj=Service("D:/python_selenium/pythonProject/drivers/chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.vtiger.com/")
elements=driver.find_elements(By.XPATH,"//a[@class='nav-link dropdown-toggle text-dark custom-nav-bar-heading-font-size']")
action=ActionChains(driver)
for ele in elements:
    action.move_to_element(ele).perform()
    time.sleep(2)