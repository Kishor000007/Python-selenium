import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/login")

#clicks on link
# driver.find_element(By.XPATH,"(//a[text()='Digital downloads '])[1]").click()

#finds number of links in webpage
all_links=driver.find_elements(By.TAG_NAME,"a")
for i in all_links:
    print(i.text)
print(f"total number of links= {len(all_links)}")
time.sleep(3)
