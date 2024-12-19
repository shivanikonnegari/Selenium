from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.automationpractice.pl/index.php?controller=authentication&back=my-account")
time.sleep(5)
driver.find_element(By.LINK_TEXT,"Women").click()
time.sleep(5)
ddown1 = driver.find_element(By.ID,"selectProductSort")
select = Select(ddown1)
time.sleep(5)
print(f"No of options available in women list box is {len(select.options)}")
for i in select.options:
    print(i.text)

num_options = len(select.options)
print(f"There are {num_options} options in the date dropdown")

for option in select.options:
    print(option.text)

dropdown = driver.find_element(By.ID, "year")
select = Select(dropdown)
time.sleep(5)

num_options = len(select.options)
print(f"There are {num_options} options in the year dropdown")

for option in select.options:
    print(option.text)