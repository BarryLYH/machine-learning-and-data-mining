from selenium import webdriver
import pandas as pd

def datetransfer(datetime):
    return datetime[-4:] + '-' + datedic[datetime.split('. ')[1][:3]] + '-' + datetime.split('.')[0]

datedic = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04',
           'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08',
           'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

databasedic = {'Name':[], 'Symbol':[], 'Startdate':[], 'Enddate':[], 'Country':[], 'Concept':[],
               'Website':[], 'Blog':[], 'Whitepaper':[], 'Facebook':[], 'Twitter':[],
               'Linkedin':[], 'Slack chat':[], 'Telegram chat':[], 'Github':[]}

infile = open('/users/barry/Desktop/tokenmarket_links.txt', 'r')
#infile = open('/users/barry/Desktop/11.txt', 'r')
data_links = infile.readlines()
infile.close()

counter = 0
for data_link in data_links:
    browser = webdriver.PhantomJS()
    url = data_link.strip('\n')
    browser.get(url)
    browser.implicitly_wait(3)
    ico1 = browser.find_element_by_class_name("col-md-6")
    ico = browser.find_elements_by_class_name('table-asset-data')
    c=0
    for part in ico:
        c += 1
    i = 1
    databasein = {'Name':'NA', 'Symbol':'NA', 'Startdate':'NA', 'Enddate':'NA', 'Country':'NA',
               'Concept':'NA', 'Website':'NA', 'Blog':'NA', 'Whitepaper':'NA', 'Facebook':'NA',
               'Twitter':'NA', 'Linkedin':'NA', 'Slack chat':'NA', 'Telegram chat':'NA', 'Github':'NA'}
    databasein['Name'] = ico1.text.split('\n')[0]
    for part in ico:
        if i == 1:
            elements = part.text.split('\n')
            databasein['Symbol'] = elements[0].split(' ')[1]
            for j in range(len(elements)):
                if elements[j] == 'Token sale opening date':
                    try:
                        d = datetransfer(elements[j+1])
                    except:
                        continue
                    databasein['Startdate'] = d
                if elements[j] == 'Token sale closing date':
                    try:
                        d = datetransfer(elements[j+1])
                    except:
                        continue
                    databasein['Enddate'] = d
                if elements[j] == 'Concept':
                    try:
                        databasein['Concept'] = elements[j+1]
                    except:
                        continue
        elif i == c:
            links = part.find_elements_by_tag_name('a')
            for link in links:
                l = link.get_attribute('href')
                l2 = link.text
                if l2 != 'What is this?':
                    databasein[l2] = l

        elif part.text.split('\n')[-1].split(' ')[0] == 'Country':
            # print(part.text)
            databasein['Country'] = part.text.split('\n')[-1].split(' ')[-1]
            if databasein['Country'][-1] == ')':
                databasein['Country'] = databasein['Country'][:-1]
        i += 1

    for index in databasein:
        databasedic[index].append(databasein[index])

    #print(databasedic)
    browser.quit()
    counter+=1
    print(counter)
    print(databasein['Name'])
    #print(databasein)
ddd = pd.DataFrame(databasedic)

ddd.to_csv('/users/barry/desktop/tokenmarket.csv')