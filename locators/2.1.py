from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.login.hiox.com/login?referrer=easycalculation.com")
driver.maximize_window()
time.sleep(5)

edit_box=driver.find_element(By.ID, "log_email")
edit_box.send_keys("shivanireddykonnegari@gmail.com")
edit_box.send_keys("Keys.RETURN")

edit_box=driver.find_element(By.NAME, "log_password")
edit_box.send_keys("Shiv@ni032002")
edit_box.send_keys("Keys.RETURN")