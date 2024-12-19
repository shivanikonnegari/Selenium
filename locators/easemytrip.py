from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://mybookings.easemytrip.com/MyBooking/MyLogin")
driver.maximize_window()
time.sleep(5)

edit_box=driver.find_element(By.ID,"txtEmailNew")
edit_box.send_keys("shivanireddykonnegari@gmail.com")
time.sleep(9)