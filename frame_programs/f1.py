#program for frame

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Firefox()
driver.get("file:///C:/Users/kisho/OneDrive/Attachments/Desktop/page2.html")
driver.maximize_window()

#Approach1:By using directly switching to the frame
# driver.find_element(By.ID,"t2").send_keys("Python")
# frame1=driver.find_element(By.ID,"f1")
# driver.switch_to.frame(frame1)
# driver.find_element(By.ID,"t1").send_keys("Selenium")


#Approach2:By using WebdriverWait method (frame_to_be_available_and_switch_to_it)
frame1=driver.find_element(By.ID,"f1")
wait=WebDriverWait(driver,10)
wait.until(EC.frame_to_be_available_and_switch_to_it(frame1))
driver.find_element(By.ID,"t1").send_keys("Selenium")