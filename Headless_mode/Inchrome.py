#Headless mode/testing means we can not see any browser/webpage ui like browser launching,clicking,navigating etc..
#This will perform/execute without showing any browser ui...
import time

from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    ser_obj=Service("D:\python_selenium\pythonProject\drivers\chromedriver.exe")
    optns=webdriver.ChromeOptions()
    optns.add_argument("--headless")           #This line we have to write to perform headless testing
    # optns.headless=True                      #This was worked in older version of selenium
    driver=webdriver.Chrome(service=ser_obj,options=optns)
    return driver

driver=headless_chrome()
driver.get("https://demo.nopcommerce.com/")
time.sleep(1)
print(driver.title)
print(driver.current_url)