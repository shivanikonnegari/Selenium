from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.easycalculation.com/index.php")
time.sleep(5)
all_links = driver.find_elements(By.XPATH,".//a")
print(len(all_links))

for links in all_links:
    print(links.text)
    if links.get_attribute('href'):
        print("link present")
    else:
        print("link not present")

all_links = driver.find_elements(By.XPATH,"(//a[normalize-space()='Love Calculator'])[1]")
print(len(all_links))
for links in all_links:
    print(links.text)
    if links.get_attribute('href'):
        print("link present")
    else:
        print("link not present")
