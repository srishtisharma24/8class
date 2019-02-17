from selenium import webdriver

driver = webdriver.Chrome()
driver.get("file:///C:/Users/Srishti.sharma2/Desktop/Selenium/webtable.html")
driver.maximize_window()
driver.implicitly_wait(5)
element=driver.find_elements_by_xpath("//*[@id='emp']/thead/tr/th")
print(len(element))
for i in element:
    print(i.text)

#fatch header from the html table under python folder