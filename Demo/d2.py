from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.webdriver import WebDriver

#here 'r' is raw string add r prefix before the string to tell python to treat as raw string,ignoring escape sequences
#we can specify path of the drivers if we can't specify then also it will work

# ser_obj=Service(r"C:\Users\kisho\Downloads\chromedriver-win64 (2)\chromedriver.exe")
ser_obj=Service(r"D:\python_selenium\pythonProject\drivers\chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
  # driver=webdriver.Chrome()
driver.get("https://admin-demo.nopcommerce.com/login")
driver.find_element(By.ID,"Email").clear()
driver.find_element(By.ID,"Password").clear()
driver.find_element(By.ID,"Email").send_keys("admin@yourstore.com")
driver.find_element(By.ID,"Password").send_keys("admin")
driver.find_element(By.ID,"RememberMe").click()
driver.find_element(By.XPATH,"//button[text()='Log in']").click()
