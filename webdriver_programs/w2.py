#program for title,current_url,page_source methods

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://www.facebook.com")
titlee=driver.title
print(titlee)
url=driver.current_url
print(url)
source=driver.page_source
print(source)