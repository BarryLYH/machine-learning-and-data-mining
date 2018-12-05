from selenium import webdriver
import pandas as pd

dic = {'name':[], 'weblink':[]}

path = 'file:///Users/Barry/Desktop/HTML/'
for i in range(1, 5):
    browser = webdriver.PhantomJS()
    add = str(i)+'.html'
    url = path + add
    browser.get(url)
    browser.implicitly_wait(3)

    name = browser.find_elements_by_xpath("//a[@target='_blank']//span[contains(@class,'ttip')]")
    web = browser.find_elements_by_xpath("//a[@target='_blank']//span[@class='ttip']//parent::a")  # web
    for j in name:
        l = j.text
        dic['name'].append(l)
    for j in web:
        l = j.get_attribute('href')
        dic['weblink'].append(l)
    browser.quit()

ddd = pd.DataFrame(dic)
ddd.to_csv('/users/barry/desktop/hah.csv')

