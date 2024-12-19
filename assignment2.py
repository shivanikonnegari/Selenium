from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()# launching url
driver.get(" https://www.makemytrip.com/cabs")
driver.maximize_window()
time.sleep(5)
actual_title = driver.title
expect_title ="Your Store"

if actual_title == expect_title:
    print("Title is verified")
else:
    print("Title is not verified")
    time.sleep(5)
Myaccount=driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[2]/a/span[1]").click()
Register=driver.find_element(By.XPATH,"/html/body/nav/div/div[2]/ul/li[2]/ul/li[1]/a").click()
actual_title = driver.title
expect_title ="Register Account"

if actual_title == expect_title:
    print("Title is verified")
else:
    print("Title is not verified")
    time.sleep(5)


