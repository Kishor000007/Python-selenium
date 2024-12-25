import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ser_obj=Service("D:/python_selenium/pythonProject/drivers/chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.myntra.com")
men_lnk=driver.find_element(By.XPATH,"(//a[text()='Men'])[2]")
action=ActionChains(driver)
action.scroll_to_element(men_lnk).perform()
time.sleep(2)