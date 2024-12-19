from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.letskodeit.com/practice")
time.sleep(2)

driver.find_element(By.XPATH,value="//input[@id='alertbtn']").click()
time.sleep(2)

driver.switch_to.alert.accept()
time.sleep(10)
driver.find_element(By.XPATH,value="//input[@id='confirmbtn']").click()
time.sleep(2)

driver.switch_to.alert.accept()
time.sleep(10)
