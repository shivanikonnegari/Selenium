from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Sigma/Downloads/Iframe.html")
driver.maximize_window()
time.sleep(5)

driver.switch_to.frame("HollandandBarrett")
driver.get("https://auth.hollandandbarrett.com/u/login")
time.sleep(5)
driver.find_element(By.ID, "username").send_keys("shivanireddykonnegari@gmail.com")
driver.find_element(By.NAME,"password").send_keys("Shiv@ni032002")
driver.find_element(By.XPATH, "/html/body/main/section/div/div/div/form/div[2]/button")
time.sleep(5)

driver.get("file:///C:/Users/Sigma/Downloads/Iframe.html")
time.sleep(5)
driver.find_element(By.XPATH,"/html/body/a").click()
driver.get("https://www.selenium.dev/")
driver.find_element(By.XPATH,"//*[@id='main_navbar']/ul/li[2]/a/span").click()
time.sleep(5)
driver.get("file:///C:/Users/Sigma/Downloads/Iframe.html")
driver.switch_to.frame("My Store")
driver.get("https://demo.opencart.com/")
time.sleep(5)
driver.find_element(By.NAME,"search").send_keys("product")
time.sleep(8)
driver.find_element(By.XPATH,"//*[@id=search]/button").click()
time.sleep(5)
driver.find_element(By.XPATH,"/html/body").click()
