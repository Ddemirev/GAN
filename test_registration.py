from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Step 1: Navigate to the registration page
driver.get("https://moneygaming.qa.gameaccount.com/")
time.sleep(2)

driver.find_element(By.LINK_TEXT, "JOIN NOW!").click()
time.sleep(2)

# Step 3: Select a title from the dropdown
title_dropdown = Select(driver.find_element(By.ID, "title"))
title_dropdown.select_by_visible_text("Mr")

# Step 4: Enter first name and surname
driver.find_element(By.NAME, "map(firstName)").send_keys("John")
driver.find_element(By.NAME, "map(lastName)").send_keys("Doe")

# Step 5: Check the terms and conditions checkbox
driver.find_element(By.NAME, "map(terms)").click()

# Step 6: Click the JOIN NOW button
driver.find_element(By.ID, "form").submit()
time.sleep(2)

# Step 7: Validate error message for missing date of birth
error_message = driver.find_element(By.XPATH, "//label[@class='error' and @for='dob']").text
assert "This field is required" in error_message, "Validation message not found!"

print("Found error message:", error_message)


# Cleanup
driver.quit()
