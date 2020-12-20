from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

mapword = input("ENTER PLACE TO SEARCH : ")
print(f"LET'S GO TO {mapword.upper()}")
driver = webdriver.Chrome()
driver.get("https://www.google.com/maps/place/" + mapword)
title = driver.title
url = driver.current_url
print(f"TITLE is {title}")
print(f"URL is {url}")
time.sleep(5)
driver.quit()
