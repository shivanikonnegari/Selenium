from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.hollandandbarrett.com/shop/vitamins-supplements/vitamins/")
time.sleep(5)

ts1 = driver.find_element(By.TAG_NAME,"img").get_attribute("src");
print(driver)

links = driver.find_elements(By.TAG_NAME,"a")
for link in links:
    print(link.text)
    print(link.get_attribute('href'))