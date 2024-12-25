import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.worldometers.info/geography/alphabetical-list-of-countries/")

#Approach1:Scroll down page by pixel
# driver.execute_script("window.scrollBy(0,3000)","")
# #It shows exact location of webpage
# value=driver.execute_script("return window.pageYOffset;")
# print(f"Number of pixels moved: {value}")

#Approach2:Scroll down the page till element is visible
# country=driver.find_element(By.XPATH,"//td[normalize-space()='India']")
# driver.execute_script("arguments[0].scrollIntoView();",country)
# value=driver.execute_script("return window.pageYOffset;")
# print(f"Number of pixels moved: {value}")

# 3)Scroll down the page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print(f"Number of pixels moved: {value}")
time.sleep(3)

#4)Scroll up to starting position
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print(f"Number of pixels moved: {value}")
time.sleep(3)

