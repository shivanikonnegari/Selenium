from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.hollandandbarrett.com/shop/vitamins-supplements/vitamins/")
time.sleep(5)

partial_link ="Vitamins"
link_element = driver.find_element(By.PARTIAL_LINK_TEXT,partial_link)
link_element.click()
time.sleep(5)

partial_link ="Supplements"
link_element = driver.find_element(By.PARTIAL_LINK_TEXT,partial_link)
link_element.click()
time.sleep(5)