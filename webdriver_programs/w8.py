from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://app.elorus.com/login/")
driver.find_element(By.LINK_TEXT,"Terms of use").click()





