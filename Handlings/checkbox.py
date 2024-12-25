import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("file:///C:/Users/kisho/OneDrive/Attachments/Desktop/sample.html")
checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))

# 1) Select all the checkboxes
#Apporoach1:
# for checkbox in checkboxes:
#     checkbox.click()

#Apporoach2:
# for checkbox in range(len(checkboxes)):
#     checkboxes[checkbox].click()

# 2) Select checkboxes by choice
# for checkbox in checkboxes:
#     idname=checkbox.get_attribute("id")
#     if idname=="c1" or idname=="c2":
#         checkbox.click()

# 3)select last 2 checkboxes
# for i in range(len(checkboxes)-2,len(checkboxes)):
#     checkboxes[i].click()

# 4) select first 2 checkboxes
for i in range(len(checkboxes)):
    if i<2:
     checkboxes[i].click()
time.sleep(3)