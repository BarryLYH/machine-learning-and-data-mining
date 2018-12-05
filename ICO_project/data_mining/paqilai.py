from selenium import webdriver
import pandas as pd

dic = {'name':[], 'fund':[], 'goal':[], 'weblink':[], 'whitepaper':[], 'startdate':[], 'enddate':[], 'Pre-sale Bonus':[],
           'Ticker':[], 'Token type':[], 'ICO Token Price':[], 'Fundraising Goal':[], 'Sold on pre-sale':[],
           'Total Tokens':[], 'Available for Token Sale':[], 'Whitelist':[], 'Know Your Customer (KYC)':[],
           'Min/Max Personal Cap':[], 'Token Issue':[], 'Accepts':[], 'Bonus for the First':[],'Сan\'t participate':[]}

datedic = {'JAN':'2018-1-', 'FEB':'2018-2-', 'MAR':'2017-3-', 'APR':'2017-4-',
           'MAY':'2017-5-', 'JUN':'2017-6-', 'JUL':'2017-7-', 'AUG':'2017-8-',
           'SEP':'2017-9-', 'OCT':'2017-10-','NOV':'2017-11-','DEC':'2017-12-'}

def getdate(time):
    start = time[0].split()
    startdate = datedic[start[1]] + start[0]
    end = time[1].split()
    enddate = datedic[end[1]] + end[0]
    return [startdate, enddate]

def getdetail(li,d):
    list = []
    for part in li:
        t = part.text
        list.append(t)
    for part in list:
        index = part.split(':')[0]
        content = part.split(':')[1]
        d[index]=content
    return d

def get_links(index_url):
    url_list = []

    browser = webdriver.PhantomJS()
    browser.get(index_url)
    browser.implicitly_wait(3)

    ico_company_list = browser.find_elements_by_class_name("ico-main-info")

    for part in ico_company_list:
        links = part.find_elements_by_tag_name('a')
        for link in links:
            l = link.get_attribute('href')
            if l in url_list: continue
            url_list.append(l)

    browser.quit()

    return url_list

def get_info(ico_list):
    browser = webdriver.PhantomJS()
    dictionary = dic
    for url in ico_list:
        try:
            d = {'Pre-sale Bonus':'NA', 'Сan\'t participate':'NA','name':'NA', 'fund':'NA', 'goal':'NA', 'weblink':'NA', 'whitepaper':'NA', 'startdate':'NA', 'enddate':'NA','Ticker':'NA', 'Token type':'NA', 'ICO Token Price':'NA', 'Fundraising Goal':'NA', 'Sold on pre-sale':'NA','Total Tokens':'NA', 'Available for Token Sale':'NA', 'Whitelist':'NA', 'Know Your Customer (KYC)':'NA','Min/Max Personal Cap':'NA', 'Token Issue':'NA', 'Accepts':'NA', 'Bonus for the First':'NA'}
            browser.get(url)
            browser.implicitly_wait(3)
            d['name'] = browser.find_element_by_class_name('ico-main-info').text.split('\n')[0]
            print(d['name'])
            d['fund'] = browser.find_element_by_class_name('money-goal').text
            d['goal'] = browser.find_element_by_class_name('goal').text.split('\n')[1]
            links = browser.find_element_by_class_name("ico-right-col").find_elements_by_tag_name('a')
            d['weblink'] = links[0].get_attribute('href')
            d['whitepaper'] = links[1].get_attribute('href')
            someone = browser.find_elements_by_class_name("list")
            for list in someone:
                try:
                    list.find_element_by_class_name('fa-calendar')
                    real = list
                except:
                    continue
            date_ico = real.text.split('\n')[0].split(':')[1].split(' – ')
            d['startdate'], d['enddate'] = getdate(date_ico)
            li = real.find_elements_by_tag_name("li")
            d = getdetail(li, d)

        except:
            continue
        print(d)
        for index in d:
            try:
                dictionary[index].append(d[index])
            except:
                continue

    browser.quit()
    return dictionary

if __name__ == '__main__':
    ico_list = get_links('https://icodrops.com/category/ended-ico/')
    #ico_list = ['https://icodrops.com/gems/' ]
    print(len(ico_list))
    dictionary = get_info(ico_list)
    print(dictionary)
    ddd = pd.DataFrame(dictionary)

    ddd.to_csv('/users/barry/desktop/ex1.csv')