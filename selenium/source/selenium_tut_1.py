from selenium import webdriver

PATH= '/home/adminuser/Documents/training/python/selenium/source/chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://www.google.com")
#driver.get("http://localhost:9515")


