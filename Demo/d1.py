from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

driver=WebDriver()
driver.implicitly_wait(30.0)
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

act_title=driver.title
exp_title="OrangeHRM"

if act_title==exp_title:
    print("Login is Passed")
else:
    print("Login is Failed")

driver.close()