#program for maximize_window,minimize_window,fullscreen_window methods

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com")
driver.maximize_window()
driver.fullscreen_window()
driver.minimize_window()
