#program for back(),forward(),refresh() methods

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://www.facebook.com")
driver.get("https://www.ajio.com")
driver.back()
driver.forward()
driver.refresh()