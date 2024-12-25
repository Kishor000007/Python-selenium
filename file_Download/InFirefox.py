import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

# Current working directory
location = os.getcwd()

def firefox_setUp():
    from selenium.webdriver.firefox.service import Service
    serv_obj=Service("D:\python_selenium\pythonProject\drivers\geckodriver.exe")
    optns=webdriver.FirefoxOptions()
    #settings                                                            #application/msword:mimetype of the document
    optns.set_preference("browser.helperApps.neverAsk.saveToDisk","application/msword") #for word/txt files
    # optns.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf") #for pdf files
    optns.set_preference("browser.download.manager.showWhenStarting",False)
     #0:saves in desktop, 1:saves in download folder, 2:saves in desired location
    optns.set_preference("browser.download.folderList",2)
    optns.set_preference("browser.download.dir",location)
    # optns.set_preference("pdfjs.disabled",True)  #to download the pdf files we add additional preference
    driver=webdriver.Firefox(service=serv_obj,options=optns)
    return driver

driver=firefox_setUp()
driver.maximize_window()
driver.get("https://practice.expandtesting.com/download")

wait = WebDriverWait(driver, 10)

# Wait for the link to be clickable
download_lnk = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/main/div[2]/div/div/div[5]/a")
))

# Click the link
download_lnk.click()

time.sleep(3)

