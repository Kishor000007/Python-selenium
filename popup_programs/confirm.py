import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/kisho/OneDrive/Attachments/Desktop/confirm.html")
driver.find_element(By.XPATH,"//button[text()='Try it']").click()
a=driver.switch_to.alert
a.accept()
time.sleep(3)