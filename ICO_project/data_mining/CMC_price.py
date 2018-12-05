from selenium import webdriver
import pandas as pd

datedic = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04',
           'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08',
           'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

infile = open('/users/barry/Desktop/cmc_links.txt', 'r')
links = infile.readlines()
infile.close()

counter = 0
for link in links:
    browser = webdriver.PhantomJS()
    url = link.strip('\n')
    browser.get(url)
    browser.implicitly_wait(3)
    #outfile = open(/users/barry/Desktop/cmc_links.txt, 'w')

    ico = browser.find_elements_by_xpath("//tr[@class='text-right']")
    title = browser.find_element_by_xpath("//meta[@property='og:title']").get_attribute('content').split(' (')[0]
    outfile = open('/users/barry/Desktop/cmc_price/'+title+'.txt', 'w')

    counter += 1
    print(counter, title)
    for part in ico:

        l = part.text
        l1 = l[:12]
        l2 = l[12:]
        l1 = l1[-4:] + '-' + datedic[l1[0:3]] + '-' + l1[4:6]
        outfile.write(l1+l2+'\n')
        #print(l1+l2)

    outfile.close()
    browser.quit()