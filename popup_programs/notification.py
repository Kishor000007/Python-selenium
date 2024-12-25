import time

from selenium import webdriver
from selenium.webdriver.chromium.options import ChromiumOptions

options=ChromiumOptions()
options.add_argument("--disable-notifications")
options.add_argument("--disable-geolocation")
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://whatmylocation.com/")
time.sleep(3)