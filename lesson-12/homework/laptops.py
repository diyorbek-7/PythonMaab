from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import json
import time

# Set up WebDriver
service = Service("C:/chromedriver/chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the website
driver.get("https://www.demoblaze.com/")
time.sleep(3)

# # Click on the 'Laptops' section
# laptops_section = driver.find_element(By.LINK_TEXT, "Laptops")
# laptops_section.click()
# time.sleep(3)
#
# laptop_data = []
#
# while True:
#     # Get all laptops on the current page
#     products = driver.find_elements(By.CLASS_NAME, "card-title")
#     prices = driver.find_elements(By.CLASS_NAME, "price-container")
#     descriptions = driver.find_elements(By.CLASS_NAME, "card-text")
#
#     for i in range(len(products)):
#         laptop = {
#             "name": products[i].text,
#             "price": prices[i].text.split(" ")[0],
#             "description": descriptions[i].text
#         }
#         laptop_data.append(laptop)
#
#     # Check if 'Next' button is available
#     try:
#         next_button = driver.find_element(By.LINK_TEXT, "Next")
#         next_button.click()
#         time.sleep(3)
#     except:
#         break
#
# # Save data to JSON file
# with open("laptops.json", "w", encoding="utf-8") as f:
#     json.dump(laptop_data, f, indent=4, ensure_ascii=False)
#
# # Close the browser
# driver.quit()
#
# print("Scraping complete. Data saved in laptops.json")
