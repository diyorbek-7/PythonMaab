from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time

driver = webdriver.Chrome()
driver.get('https://www.demoblaze.com/')
time.sleep(5)
laptop_section = driver.find_element(By.LINK_TEXT,'Laptops')
laptop_section.click()
time.sleep(5)

laptops_data=[]
while True:
    products = driver.find_element(By.CLASS_NAME,'card-title')
    prices = driver.find_elements(By.CLASS_NAME, "price-container")
    descriptions = driver.find_elements(By.CLASS_NAME, "card-text")

    for i in range(len(products)):
        laptop = {
            'name':products[i].text,
            'price':products[i].text.split(' ')[0],
            'description':descriptions[i].text
        }
        laptops_data.append(laptop)
        try:
            next_button = driver.find_element(By.LINK_TEXT, "Next")
            next_button.click()
            time.sleep(3)
        except:
            break
with open("laptops.json", "w", encoding="utf-8") as f:
    json.dump(laptop_data, f, indent=4, ensure_ascii=False)

driver.quit()

