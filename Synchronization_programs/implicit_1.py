from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.actitime.com/")
driver.find_element(By.XPATH,"//a[text()='Get started']").click()