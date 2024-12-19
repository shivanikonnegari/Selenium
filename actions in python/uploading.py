from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(5)

driver.execute_script("window.scrollBy(0,1300);")

driver.find_element(By.ID,"singleFileInput").send_keys("C:\\Users\\Sigma\\Pictures\\screenshots\\Screenshot (11).png")
