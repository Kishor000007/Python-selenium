import time

from selenium import webdriver

def headless_firefox():
    from selenium.webdriver.firefox.service import Service
    ser_obj=Service("D:\python_selenium\pythonProject\drivers\geckodriver.exe")
    optns=webdriver.FirefoxOptions()
    optns.add_argument("--headless")           #This line we have to write to perform headless testing
    driver=webdriver.Firefox(service=ser_obj,options=optns)
    return driver

driver=headless_firefox()
driver.get("https://demo.nopcommerce.com/")
time.sleep(1)
print(driver.title)
print(driver.current_url)