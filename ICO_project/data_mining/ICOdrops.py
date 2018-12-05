from selenium import webdriver
import pandas as pd

dictionary = {'Name':[], 'Raised_money':[], 'Target':[], 'Website':[], 'Whitepaper':[],
             'Startdate':[], 'Enddate':[], 'Ticker':[], 'Token type':[], 'ICO Token Price':[],
             'Fundraising Goal':[], 'Sold on pre-sale':[], 'Total Tokens': [],
             'Available for Token Sale':[], 'Whitelist': [], 'Know Your Customer (KYC)':[],
             'Min/Max Personal Cap':[], 'Сan\'t participate':[], 'Pre-sale Bonus':[],

             'Token Issue': [], 'Accepts':[], 'Bonus for the First':[],
             't.me':[], 'medium':[], 'facebook': [], 'twitter':[], 'bitcointalk':[],
             'linkedin':[], 'instagram':[], 'youtube': [], 'reddit':[], 'discord':[],
             'github':[], 'slack': [], 'chat':[], 'google':[]}



datedic = {'JAN':'2018-1-', 'FEB':'2018-2-', 'MAR':'2017-3-', 'APR':'2017-4-',
           'MAY':'2017-5-', 'JUN':'2017-6-', 'JUL':'2017-7-', 'AUG':'2017-8-',
           'SEP':'2017-9-', 'OCT':'2017-10-','NOV':'2017-11-','DEC':'2017-12-'}

def getdate(time):
    try:
        start = time[0].split()
        startdate = datedic[start[1]] + start[0]
        end = time[1].split()
        enddate = datedic[end[1]] + end[0]
        return [startdate, enddate]
    except:
        startdate = ' '
        enddate = ' '

    return [startdate, enddate]

def getdetail(li,d):
    list = []
    for part in li:
        t = part.text
        list.append(t)
    for part in list:
        index = part.split(':')[0]
        content = part.split(':')[1]
        if index in d:
            d[index]=content
    return d

infile = open('/users/barry/Desktop/ICOdrops_links.txt', 'r')
links = infile.readlines()
infile.close()


counter = 0
for link in links:
    counter += 1
    print(counter)
    print(link)

    d = {'Name':' ', 'Raised_money':' ', 'Target':' ', 'Website':' ', 'Whitepaper':' ',
         'Startdate':' ', 'Enddate':' ', 'Ticker':' ', 'Token type':' ', 'ICO Token Price':' ',
         'Fundraising Goal':' ', 'Sold on pre-sale':' ','Total Tokens':' ',
         'Available for Token Sale':' ', 'Whitelist':' ', 'Сan\'t participate':' ',
         'Know Your Customer (KYC)':' ','Min/Max Personal Cap':' ',
         'Pre-sale Bonus':'',
         'Token Issue':' ', 'Accepts':' ', 'Bonus for the First':' ',
         't.me':' ', 'medium':' ', 'facebook':' ', 'twitter':' ', 'bitcointalk':' ',
         'linkedin':' ', 'instagram':' ', 'youtube':' ', 'reddit':' ', 'discord':' ',
         'github':' ', 'slack':' ', 'chat':' ', 'google':' '}

    browser = webdriver.PhantomJS()
    url = link.strip('\n')
    browser.get(url)
    browser.implicitly_wait(3)

    d['Name'] = browser.find_element_by_class_name('ico-main-info').text.split('\n')[0]
#    d['Raised_money'] = browser.find_element_by_class_name('money-goal').text
    try:
        d['Target'] = browser.find_element_by_class_name('goal').text.split('\n')[1]
    except:
        d['Target'] = ' '
    links22 = browser.find_element_by_class_name("ico-right-col").find_elements_by_tag_name('a')
    try:
        d['Website'] = links22[0].get_attribute('href')
    except:
        d['Website'] = ' '
    try:
        d['Whitepaper'] = links22[1].get_attribute('href')
    except:
        d['Whitepaper'] = ' '
    #  someone = browser.find_elements_by_class_name("list")
 #   for list in someone:
#        try:
#            list.find_element_by_class_name('fa-calendar')
#            real = list
#        except:
#            continue
#    date_ico = real.text.split('\n')[0].split(':')[1].split(' – ')
#    d['Startdate'], d['Enddate'] = getdate(date_ico)
#    li = real.find_elements_by_tag_name("li")
#    d = getdetail(li, d)
#
#    links1 = browser.find_element_by_class_name('soc_links').find_elements_by_tag_name('a')
#    for link in links1:
#        l = link.get_attribute('href')
#        for index in d:
#            if index in l:
#                d[index] = l
#                break

    for index in d:
        dictionary[index].append(str(d[index]))
    browser.quit()

ddd = pd.DataFrame(dictionary)
ddd = ddd[['Name', 'Raised_money', 'Target', 'Website', 'Whitepaper',
         'Startdate', 'Enddate', 'Ticker', 'Token type', 'ICO Token Price',
         'Fundraising Goal', 'Sold on pre-sale', 'Total Tokens',
         'Available for Token Sale', 'Whitelist', 'Know Your Customer (KYC)',
         'Min/Max Personal Cap',

         'Token Issue', 'Accepts', 'Bonus for the First',
         't.me', 'medium', 'facebook', 'twitter', 'bitcointalk',
         'linkedin', 'instagram', 'youtube', 'reddit', 'discord',
         'github', 'slack', 'chat', 'google']]
ddd.to_csv('/users/barry/desktop/ICOdrops.csv')