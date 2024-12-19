from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.letskodeit.com/practice")
time.sleep(5)
Radio_buttons = driver.find_elements(By.XPATH,"")
print(len(Radio_buttons))