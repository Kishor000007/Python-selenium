import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://jqueryui.com/slider/")
Frame=driver.find_element(By.XPATH,"//*[@id='content']/iframe")
driver.switch_to.frame(Frame)
slider=driver.find_element(By.XPATH,"//*[@id='slider']/span")
print("Location of slider before moving")
print(slider.location)

action=ActionChains(driver)
action.drag_and_drop_by_offset(slider,100,0).perform()
print("Location of slider before moving")
print(slider.location)
time.sleep(3)