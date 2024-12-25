import time

from selenium import webdriver

def headless_edge():
    from selenium.webdriver.edge.service import Service
    ser_obj=Service("D:\python_selenium\pythonProject\drivers\msedgedriver.exe")
    optns=webdriver.EdgeOptions()
    optns.add_argument("--headless")           #This line we have to write to perform headless testing
    driver=webdriver.Edge(service=ser_obj,options=optns)
    return driver

driver=headless_edge()
driver.get("https://demo.nopcommerce.com/")
time.sleep(1)
print(driver.title)
print(driver.current_url)