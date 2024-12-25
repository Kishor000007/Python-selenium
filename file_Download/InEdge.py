import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Current working directory
location = os.getcwd()

def edge_setUp():
    from selenium.webdriver.edge.service import Service
    serv_obj = Service("D:/python_selenium/pythonProject/drivers/msedgedriver.exe")
    # Set preferences for Edge
    preferences = {"download.default_directory":location}
    # preferences = {"download.default_directory": location, "plugins.always_open_pdf_externally":True}  #it is for pdf document
    optns = webdriver.EdgeOptions()
    optns.add_experimental_option("prefs", preferences)
    driver = webdriver.Edge(service=serv_obj, options=optns)
    return driver

# Initialize the driver
driver = edge_setUp()
driver.maximize_window()
driver.get("https://practice.expandtesting.com/download")
driver.implicitly_wait(10)

txtfile=driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div/div[28]/a")
action=ActionChains(driver)
action.scroll_to_element(txtfile).perform()
driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div/div[28]/a").click()

time.sleep(5)