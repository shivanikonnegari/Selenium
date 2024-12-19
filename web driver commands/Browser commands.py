from selenium import webdriver
from selenium.webdriver.common.by import By
import time
baseurl = "https://www.linkedin.com/feed/"
driver = webdriver.Chrome()
driver.maximize_window()
driver.get(baseurl)
title = driver.title
print("Title of the web page is:" + title)
currenturl = driver.current_url
print("current url of the web page is: + currenturl")
driver.refresh()
print("Browser Refreshed 1st time")
driver.get(driver.current_url)
print("Browser Reefreshed 2nd time")
driver.back()
print("Go one stop back in browser history ")
currenturl = driver.current_url
print("current url of the web page is:" + currenturl)
pageSource = driver.page_source
print(pageSource.encode("utf-8"))
driver.quit()


