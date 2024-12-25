#In our automation we just check that we can add or delete and to get details of the cookies....
#Some websites doesn't allow us to add or delete the cookies....

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

ser_obj=Service("D:/python_selenium/pythonProject/drivers/chromedriver.exe")
driver=webdriver.Chrome(service=ser_obj)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.nopcommerce.com/")

#Capture cookies from the browser
cookie=driver.get_cookies()
print(f"Number of Cookies: {len(cookie)}")  #3

# Print details of cookies
# for c in cookie:
#     # print(c)
#     print(c.get("name"),":",c.get("value"))

#Add new cookie to the browser
driver.add_cookie({"name":"MyCookie", "value":"9876534"})
cookie=driver.get_cookies()
print(f"Number of cookies after adding Cookies: {len(cookie)}")  #4

#Delete the specific cookie
driver.delete_cookie("MyCookie")
cookie=driver.get_cookies()
print(f"Number of cookies after deleting one Cookie: {len(cookie)}")  #3

#Deleting all the cookies
driver.delete_all_cookies()
cookie=driver.get_cookies()
print(f"Number of cookies after deleting one Cookie: {len(cookie)}") #0