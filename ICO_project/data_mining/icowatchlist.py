from selenium import webdriver
import pandas as pd

infile = open('/users/barry/Desktop/icowatchlist.txt', 'r')
data_links = infile.readlines()
infile.close()

for data_link in data_links:
    browser = webdriver.PhantomJS()
    url = data_link.strip('\n')
    browser.get(url)
    browser.implicitly_wait(3)

