import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/datepicker/")
driver.switch_to.frame(0)

#Approach1:
#most of the time we can direct send date,month,year through sendkeys method.But some application don't allow
# driver.find_element(By.ID,"datepicker").send_keys("05/13/2002")    #format:mm/dd/yyyy

# Approach 2: Logic to select date when send_keys is not allowed
driver.find_element(By.ID, "datepicker").click()

month = "May"
date = "13"
year = "2022"

while True:
    # Fetch the current month and year displayed in the datepicker
    mon = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    yr = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon == month and yr == year:
        break
    else:
        # Navigate to the previous month
        driver.find_element(By.XPATH, "//*[@id='ui-datepicker-div']/div/a[1]/span").click()  #backward arrowmark
        # driver.find_element(By.XPATH,"//*[@id='ui-datepicker-div']/div/a[2]/span").click()  #forward arrowmark
        time.sleep(0.5)  # Small delay to allow DOM to update

# Select the specified date
dates = driver.find_elements(By.XPATH, "//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for element in dates:
    if element.text == date:
        element.click()
        break

# Add a small delay to observe the selected date before closing
time.sleep(2)
driver.quit()


