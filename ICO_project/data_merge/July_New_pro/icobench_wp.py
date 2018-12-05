from selenium import webdriver
import pandas as pd


def extraction(contents):
    price = 'NA'
    for i in range(len(contents)):
        if contents[i] == 'Price in ICO':
            price = contents[i+1]

    return price

infile = open('/users/barry/Desktop/bench.txt', 'r')
links = infile.readlines()
infile.close()

outfile = open('/users/barry/desktop/data2.txt', 'a+')

counter = 0
for link in links:

    counter += 1
    print(counter)
    browser = webdriver.PhantomJS()
    url = link.strip('\n')
    browser.get(url)
    browser.implicitly_wait(3)
    js = "document.getElementById('financial').style.display='block'"
    try:
        browser.execute_script(js)  # 执行JS
    except:
        pass

    name = browser.find_element_by_class_name("name").text.split('\n')[0]
    content = browser.find_elements_by_class_name("col_2")
    contents = []
    for part in content:
        contents.append(part.text)
    price= extraction(contents)
    wp = 'NA'
    try:
        wp = browser.find_element_by_xpath("//a[contains(text(),'White paper')]").get_attribute('href')
    except:
        pass
    print(name, wp, price)
    outfile.write(name+'++++'+wp+'++++'+price)
    outfile.write('\n')
    outfile.flush()


    browser.quit()