import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Current working directory
location = os.getcwd()

def chrome_setUp():
    from selenium.webdriver.chrome.service import Service
    serv_obj = Service("D:/python_selenium/pythonProject/drivers/chromedriver.exe")
    # Set preferences for Chrome
    preferences = {"download.default_directory":location}  #it is for word/txt document
    # preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally":True}  #it is for pdf document
    optns = webdriver.ChromeOptions()
    optns.add_experimental_option("prefs", preferences)
    driver = webdriver.Chrome(service=serv_obj, options=optns)
    return driver

# Initialize the driver
driver = chrome_setUp()
driver.get("https://practice.expandtesting.com/download")
driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Wait for the link to be clickable
download_lnk = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/main/div[2]/div/div/div[28]/a")
))
time.sleep(3)
# Click the link
download_lnk.click()

time.sleep(3)


