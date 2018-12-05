from selenium import webdriver
import pandas as pd

browser = webdriver.PhantomJS()
url = 'https://icobench.com/ico/aenco'
browser.maximize_window()
browser.get(url)
browser.implicitly_wait(3)
js = "document.getElementById('team').style.display='block'"
browser.execute_script(js) #执行JS
#ico = browser.find_elements_by_class_name('dt-center')
#ico = browser.find_elements_by_xpath("//a[@target='_blank']//span[@class='ttip']//parent::a") #web
#ico = browser.find_elements_by_xpath("//a[@target='_blank']//span[contains(@class,'ttip')]") #Name
ico = browser.find_element_by_xpath("//a[contains(text(),'White paper')]")
#ico = browser.find_element_by_xpath("//a[@onclick='ga('send', 'event', 'ICOprofile', 'Tab - Whitepaper');']")
#ico = browser.find_elements_by_class_name("details-text-medium")
#ico = browser.find_element_by_class_name("name")

print(ico.get_attribute('href'))



'''
c= 0
for part in ico:
    c += 1
    print(part.text)
'''
#print(c)
'''
links = ico.find_elements_by_tag_name('a')
for link in links:
    l = link.get_attribute('href')
    print(l)
'''
browser.quit()