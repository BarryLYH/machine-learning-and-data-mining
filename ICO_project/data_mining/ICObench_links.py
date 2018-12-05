from selenium import webdriver
import pandas as pd

infile = open('/users/barry/Desktop/links.txt', 'r')
links = infile.readlines()
infile.close()

outfile = open('/users/barry/Desktop/icobench_links.txt', 'w')

list = []
counter = 0
for link in links:

    counter += 1
    print(counter)
    browser = webdriver.PhantomJS()
    url = link.strip('\n')
    browser.get(url)
    browser.implicitly_wait(3)

    ico = browser.find_elements_by_class_name("image")

    for part in ico:
        l = part.get_attribute('href')
        if l not in list:
            outfile.write(l + '\n')
            list.append(l)
            print(l)
    browser.quit()
outfile.close()