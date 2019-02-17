from selenium import webdriver
driver=webdriver.Chrome()
driver.get("file:///C:/Users/Srishti.sharma2/Desktop/Selenium/webtable.html")
driver.maximize_window()
driver.implicitly_wait(5)
element1=driver.find_element_by_xpath("//*[@id='emp']/thead/tr/th[1]")
print(element1.text)
element=driver.find_elements_by_xpath("//*[@id='emp']/tbody/tr/td[1]")
for i in element:
    print(i.text)

#get eid and respective id (eid,1,2)
