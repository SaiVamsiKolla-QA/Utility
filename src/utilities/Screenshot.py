import time
import os
from datetime import datetime

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a directory for screenshots if it doesn't exist
screenshots_dir = "Screenshots"
if not os.path.exists(screenshots_dir):
    os.makedirs(screenshots_dir)

# Function to take screenshot with timestamp
def take_screenshot(driver, name):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{screenshots_dir}/{timestamp}_{name}.png"
    driver.save_screenshot(filename)
    print(f"Screenshot saved: {filename}")
    # Attach to Allure report if allure is available
    try:
        with open(filename, "rb") as file:
            allure.attach(
                file.read(),
                name=filename,
                attachment_type=allure.attachment_type.PNG
            )
    except Exception as e:
        print(f"Could not attach to Allure report: {e}")

    return filename


# Start the browser session
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://thewholetruthfoods.com")

# Take initial screenshot
take_screenshot(driver, "homepage")

# Scroll to the bottom
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)

# Take screenshot after scrolling
take_screenshot(driver, "end")

# Quit the browser
driver.quit()