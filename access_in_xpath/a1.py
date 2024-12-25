# from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
# from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver=WebDriver()
driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.implicitly_wait(20.0)
driver.maximize_window()

#Self
txt_msg=driver.find_element(By.XPATH,"//a[normalize-space()='Swan Energy Ltd.']/self::a").text
print(txt_msg)

# parent
txt_msg=driver.find_element(By.XPATH,"//a[normalize-space()='Swan Energy Ltd.']/parent::td").text
print(txt_msg)

# ancestor
txt_msg=driver.find_element(By.XPATH,"//a[normalize-space()='Swan Energy Ltd.']/ancestor::tr").text
print(txt_msg)

#child
txt_msg=driver.find_elements(By.XPATH,"//a[normalize-space()='Swan Energy Ltd.']/ancestor::tr/child::td")
print(len(txt_msg))

#descendant
descendants=driver.find_elements(By.XPATH,"//a[normalize-space()='Swan Energy Ltd.']/ancestor::tr/descendant::*")
print(f"Number of descendants={len(descendants)}")

#following
followings=driver.find_elements(By.XPATH,"//a[normalize-space()='Swan Energy Ltd.']/ancestor::tr/following::*")
print(f"Number of followings={len(followings)}")

#following-sibling
following_siblings=driver.find_elements(By.XPATH,"//a[normalize-space()='Swan Energy Ltd.']/ancestor::tr/following-sibling::*")
print(f"Number of following_siblings={len(following_siblings)}")

# preceding
precedings=driver.find_elements(By.XPATH,"//a[normalize-space()='Swan Energy Ltd.']/ancestor::tr/preceding::*")
print(f"Number of precedings={len(precedings)}")

#preceding-sibling
preceding_siblings=driver.find_elements(By.XPATH,"//a[normalize-space()='Swan Energy Ltd.']/ancestor::tr/preceding-sibling::*")
print(f"Number of preceding_siblings={len(preceding_siblings)}")