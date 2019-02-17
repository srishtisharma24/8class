from selenium import webdriver
driver=webdriver.Chrome()
driver.get("http://facebook.com")
driver.maximize_window()
driver.implicitly_wait(5)
element=driver.find_elements_by_tag_name("//a")

for data in element:
    print(len(element))
#find the ancor link on webpage