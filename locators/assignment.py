from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.easycalculation.com/index.php")
time.sleep(5)

driver.find_element(By.XPATH,"//*[@id='alarmContentDisplay']/div[1]/div[6]/div[2]/div[1]/ul[1]/li[1]/a").click()
time.sleep(5)

all_links = driver.find_elements(By.XPATH,".//a")
print(len(all_links))
time.sleep(5)





