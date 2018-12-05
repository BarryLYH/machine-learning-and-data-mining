from selenium import webdriver
import pandas as pd

databasedic = {'Name':[], 'Symbol':[], 'Circulating Supply':[], 'Max Supply':[], 'Website':[],
               'Website 2':[], 'Explorer':[], 'Explorer 2':[], 'Explorer 3':[],'Message Board':[],
               'Message Board 2':[], 'Message Board 3':[], 'Source Code':[],'Announcement':[],
               'Chat':[], 'Chat 2':[]}

infile = open('/users/barry/Desktop/links/cmc_links.txt', 'r')
links = infile.readlines()
infile.close()


worn = []
counter = 0
for link in links:
    counter += 1
    print(counter)
    print(link)

    browser = webdriver.PhantomJS()
    url = link.strip('\n')
    browser.get(url)
    browser.implicitly_wait(3)

    dicin = {'Name':'NA', 'Symbol':'NA', 'Circulating Supply':'NA', 'Max Supply':'NA',
            'Website':'NA', 'Website 2':'NA', 'Explorer':'NA', 'Explorer 2':'NA',
            'Explorer 3':'NA','Message Board':'NA', 'Announcement':'NA', 'Chat':'NA',
            'Message Board 2':'NA', 'Message Board 3':'NA', 'Source Code':'NA',
            'Chat 2':'NA'}

    title = browser.find_element_by_xpath("//meta[@property='og:title']").get_attribute('content').split(' historical data ')[0]
    info = browser.find_elements_by_class_name("details-text-medium")
    webs = browser.find_elements_by_xpath("//a[@rel='noopener']")

    try:
        dicin['Name'] = title.split(' (')[0]
        dicin['Symbol'] = title.split(' (')[1][:-1]
    except:
        worn.append(link)

    for i in range(len(info)):
        if info[i].text == 'Circulating Supply':
            dicin['Circulating Supply'] = info[i + 1].text
        elif info[i].text == 'Max Supply':
            dicin['Max Supply'] = info[i + 1].text

    for part in webs:
        web = part.get_attribute('href')
        if part.text in dicin:
            dicin[part.text] = web


    for index in dicin:
        databasedic[index].append(dicin[index])
    print(dicin)

    browser.quit()


print(worn)