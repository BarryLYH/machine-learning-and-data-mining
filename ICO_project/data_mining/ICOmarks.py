from selenium import webdriver
import pandas as pd


datedic = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04',
           'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08',
           'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

databasedic = {'Name':[], 'Symbol':[], 'Pre-Start':[], 'Pre-End':[], 'Start':[], 'End':[], 'Bounty':[],
               'Country':[], 'Concept':[], 'Platform':[], 'Type':[], 'Raised':[], 'Price':[], 'Token Type':[],
               'Accepting':[], 'Medium':[], 'Bitcointalk':[],  'Website':[], 'Whitepaper':[], 'Slack':[],
               'Facebook':[], 'Twitter':[],'Linkedin':[], 'Telegram':[], 'Github':[], 'Reddit':[], }

def dateprocess(date):
    parts = date.split(' ')
    return parts[2]+'-'+datedic[parts[1]] + '-' +parts[0]



infile = open('/users/barry/Desktop/ICOmarks_links.txt', 'r')
#infile = open('/users/barry/Desktop/11.txt', 'r')
web_links = infile.readlines()
infile.close()
counter = 0

for web in web_links:
    counter += 1
    print(counter)
    browser = webdriver.PhantomJS()
    url = web.strip('\n')
    browser.get(url)
    browser.implicitly_wait(3)

    databasein = {'Name':'NA', 'Symbol':'NA', 'Pre-Start':'NA', 'Pre-End':'NA', 'Start':'NA', 'End':'NA', 'Token Type':'NA',
                   'Country':'NA', 'Concept':'NA', 'Platform':'NA', 'Type':'NA', 'Raised':'NA', 'Price':'NA', 'Slack':'NA',
                   'Accepting':'NA', 'Medium':'NA', 'Bitcointalk':'NA', 'Website':'NA', 'Whitepaper':'NA', 'Bounty':'NA',
                   'Facebook':'NA', 'Twitter':'NA', 'Linkedin':'NA', 'Telegram':'NA', 'Github':'NA', 'Reddit':'NA', }

    name = browser.find_element_by_xpath("//h1[@itemprop='name']").text
    print(name)
    content = browser.find_element_by_xpath("//div[@class='company-description']").text
    databasein['Name'] = name
    databasein['Concept'] = content
    ico = browser.find_elements_by_class_name("icoinfo-block")
    general = ico[0]
    socialmedia = ico[3]

    links = general.find_elements_by_tag_name('a')
    for link in links:
        l = link.get_attribute('href')
        l2 = link.text
        if l2 == 'Visit':
            databasein['Website'] = l
            continue
        if l2 == 'Read':
            databasein['Whitepaper']= l
            continue
        if l2 == 'Bounty':
            databasein['Bounty'] = l

    data= []
    for i in range(3):
        l = ico[i].text.split('\n')
        for part in l:
            data.append(part)

    for i in range(len(data)):
        if data[i] == 'Pre-sale Time:':
            try:
                date = data[i + 1].split('-')
                databasein['Pre-Start'] = dateprocess(date[0])
                databasein['Pre-End'] = dateprocess(date[1][1:])
            except:
                continue
        elif data[i] == 'ICO Time:':
            try:
                date = data[i + 1].split('-')
                databasein['Start'] = dateprocess(date[0])
                databasein['End'] = dateprocess(date[1][1:])
            except:
                continue
        elif data[i] == 'Country:':
            databasein['Country'] = data[i+1]
        elif data[i] == 'Ticker:':
            databasein['Symbol'] = data[i+1]
        elif data[i] == 'Platform:':
            databasein['Platform'] = data[i+1]
        elif data[i] == 'Token Type:':
            databasein['Token Type'] = data[i+1]
        elif data[i] == 'Raised':
            databasein['Raised'] = data[i+1]
        elif data[i] == 'Price:':
            databasein['Price'] = data[i+1]
        elif data[i] == 'Accepting:':
            databasein['Accepting'] = data[i+1]

    links = socialmedia.find_elements_by_tag_name('a')
    for link in links:
        l = link.get_attribute('href')
        l2 = link.text
        databasein[l2] = l

    for index in databasein:
        databasedic[index].append(databasein[index])
    print(databasein)

    browser.quit()

ddd = pd.DataFrame(databasedic)
ddd.to_csv('/users/barry/desktop/ICOmarks.csv')