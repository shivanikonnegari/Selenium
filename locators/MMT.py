from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://www.makemytrip.com/cabs")
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH,"//img[@alt='signInByMailButton']").click()
driver.find_element(By.XPATH,"//input[@placeholder='Enter Email Address']").send_keys("shivanireddykonnegari@gmail.com")
time.sleep(3)
driver.find_element(By.XPATH,"//span[normalize-space()='Continue']").click()
time.sleep(3)
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("Shiv@ni032002")
time.sleep(3)
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/section[1]/form[1]/div[2]/button[1]").click()
time.sleep(3)
driver.find_element(By.XPATH,"//span[@class='mybizLoginClose']").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/label[1]/span[1]").send_keys("Bangalore")
