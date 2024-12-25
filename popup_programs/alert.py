import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/kisho/OneDrive/Attachments/Desktop/alert.html")
driver.find_element(By.XPATH,"//button[text()='Try it']").click()
wait=WebDriverWait(driver,10)
wait.until(EC.alert_is_present())
a=driver.switch_to.alert
print(a.text)
a.accept()
time.sleep(3)
