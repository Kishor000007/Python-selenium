import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/kisho/OneDrive/Attachments/Desktop/prompt.html")
driver.find_element(By.XPATH,"//button[text()='Try it']").click()
a=driver.switch_to.alert
print(a.text)
a.send_keys("Kishor")
a.accept()
time.sleep(3)
