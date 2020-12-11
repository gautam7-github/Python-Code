from selenium import webdriver

map_search = input("ENTER GOOGLE MAPS SEARCH : ")
driver = webdriver.Chrome()
driver.get("https://www.google.com/maps/place/" + map_search)
driver.implicitly_wait(5)
if input("'exit' for EXITING : ") == "exit":
    driver.quit()
else:
    pass

