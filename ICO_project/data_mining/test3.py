from selenium import webdriver

browser = webdriver.PhantomJS()
url = 'https://coincheckup.com/coins/tenx/charts'
browser.get(url)
#browser.implicitly_wait(3)
#x = browser.find_element_by_xpath("//li[@data-range-key='Forever']").click()
ico = browser.find_element_by_xpath("//li[@*='Forever']")
print(ico.text)


'''
f = open('/users/barry/desktop/2.html', 'a')
f.writelines(y)
f.close()
'''