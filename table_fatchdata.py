from selenium import webdriver
driver=webdriver.Chrome()
driver.get("file:///C:/Users/Srishti.sharma2/Desktop/Selenium/webtable.html")
driver.maximize_window()
driver.implicitly_wait(5)