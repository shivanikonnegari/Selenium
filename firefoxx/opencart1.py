from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://demo.opencart.com/")
driver.maximize_window()
driver.minimize_window()
time.sleep(8)
actual_title = driver.title
expect_title ="OpenCart-Open Source Shopping Cart Solution"

if actual_title == expect_title:
    print("Title is verified")
else:
    print("Title is not verified")