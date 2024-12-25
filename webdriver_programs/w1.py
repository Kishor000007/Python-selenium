#program for get(),close() and quit()

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.youtube.com")
# driver.close()
driver.quit()