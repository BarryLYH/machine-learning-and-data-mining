from selenium import webdriver
import pandas as pd

browser = webdriver.PhantomJS()
url = '/users/barry/desktop/11.html'
browser.get(url)
browser.implicitly_wait(3)
outfile = open('/users/barry/Desktop/cmc_links.txt', 'w')
#ico = browser.find_elements_by_class_name('dt-center')
#ico = browser.find_elements_by_xpath("//a[@target='_blank']//span[@class='ttip']//parent::a") #web
#ico = browser.find_elements_by_xpath("//a[@target='_blank']//span[contains(@class,'ttip')]") #Name
#ico = browser.find_elements_by_xpath("//span[contains(text(),'Completed')]/..")
ico = browser.find_elements_by_xpath("//a[@class='link-secondary']")

list = []
c = 0
for part in ico:
    l = part.get_attribute('href')
    #
    if l not in list:
        outfile.write(l+ 'historical-data/?start=20130428&end=20181205' + '\n')
        list.append(l)
        print(l+ 'historical-data/?start=20130428&end=20181205')
        c += 1

print(c)
outfile.close()
browser.quit()

