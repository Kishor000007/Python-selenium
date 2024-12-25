from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Maximize the window
driver.maximize_window()

# Set up an explicit wait
wait = WebDriverWait(driver, 10)

# Navigate to the login page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Wait for the page title to be correct
wait.until(EC.title_is("OrangeHRM"))

# Wait until the username field is visible
username_field = wait.until(EC.visibility_of_element_located((By.NAME, "username")))

# Now interact with the username and password fields
username_field.send_keys("Admin")

# Wait for the password field to be visible and then send the password
password_field = wait.until(EC.visibility_of_element_located((By.NAME, "password")))
password_field.send_keys("admin123")

# Wait for the login button to be clickable and click it
login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Login')]")))
login_button.click()


