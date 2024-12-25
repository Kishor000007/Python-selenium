from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os

ser_obj=Service("D:/python_selenium/pythonProject/drivers/chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.facebook.com")
# driver.save_screenshot(r"D:\python_selenium\pythonProject\ScreenShot_program\facebook.png")
# driver.save_screenshot(os.getcwd()+"\\facebook.png")
# driver.get_screenshot_as_file(os.getcwd()+"\\facebook.png")
# driver.get_screenshot_as_base64(os.getcwd()+"\\facebook.png") #saves in binary format
driver.get_screenshot_as_png(os.getcwd()+"\\facebook.png")