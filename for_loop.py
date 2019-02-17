from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://facebook.com")
driver.maximize_window()
driver.implicitly_wait(5)
element=driver.find_elements_by_xpath("//input[@type='text' or @type='password' or @type='email']")
for data in element:
    print('Qspider')

#write qspider in all text feild
#inpute use text feild