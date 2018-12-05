from selenium import webdriver
import pandas as pd

datedic = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04',
           'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08',
           'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

def timeprocess(date):
    days = date.split(' ')
    return days[2]+'-'+datedic[days[1]]+'-'+days[0][:-2]


def extraction(contents):
    symbol = price = country = startdate = enddate = 'NA'
    for i in range(len(contents)):
        if contents[i] == 'Token':
            symbol = contents[i+1]
        elif contents[i] == 'Price in ICO':
            price = contents[i+1]
        elif contents[i] == 'Country':
            country = contents[i+1]
        elif contents[i] == 'ICO start':
            startdate = timeprocess(contents[i+1])
        elif contents[i] == 'ICO end':
            enddate = timeprocess(contents[i+1])

    return [symbol, price, country, startdate, enddate]

def extract(info):
    platform = type = amount = accept =distri = soft = hard = raised = 'NA'
    for i in range(len(info)):
        if info[i] == 'Platform':
            platform= info[i+1]
        elif info[i] == 'Type':
            type = info[i+1]
        elif info[i] == 'Tokens for sale':
            amount = info[i+1]
        elif info[i] == 'Accepting':
            accept = info[i+1]
        elif info[i] == 'Distributed in ICO':
            distri = info[i+1]
        elif info[i] == 'Soft cap':
            soft = info[i+1]
        elif info[i] == 'Hard cap':
            hard = info[i+1]
        elif info[i] == 'Raised':
            raised = info[i+1]
    return [platform, type, amount, accept, distri, soft, hard,raised]

infile = open('/users/barry/Desktop/bench.txt', 'r')
links = infile.readlines()
infile.close()

list = []

outfile = open('/users/barry/desktop/icobench_data2.txt', 'a+')

counter = 0
for link in links:

    counter += 1
    print(counter)
    browser = webdriver.Chrome()
    url = link.strip('\n')
    browser.get(url)
    browser.implicitly_wait(3)
    js = "document.getElementById('financial').style.display='block'"
    browser.execute_script(js)  # 执行JS
    js = "document.getElementById('team').style.display='block'"
    browser.execute_script(js)

    name = browser.find_element_by_class_name("name").text.split('\n')[0]

    content = browser.find_elements_by_class_name("col_2")
    contents = []
    for part in content:
        contents.append(part.text)
    symbol, price, country, startdate, enddate = extraction(contents)
    socials = ''
    try:
        social = browser.find_element_by_class_name("socials")
        webs = social.find_elements_by_tag_name('a')
        for w in webs:
            ww = w.get_attribute('href')
            socials = socials + ww +'\n'
    except:
        pass
    info = browser.find_element_by_class_name("box").text.split('\n')
    platform, type, amount, accept, distri, soft, hard, raised = extract(info)

    bonus = 'NA'
    try:
        bonus = browser.find_element_by_class_name("bonus_text").text
    except:
        pass

    teaminfo = browser.find_element_by_xpath("//div[@class='tab_content' and @id='team']")
    team = teaminfo.text.split('\n')
    linked = []
    try:
        linkeds = teaminfo.find_elements_by_tag_name('a')
        for lin in linkeds:
            li = lin.get_attribute('href')
            if 'linkedin' in li:
                linked.append(li)
        c = 0
        for i in range(len(team)):
            if team[i] == 'LinkedIn':
                team[i] = linked[c]
                c += 1
    except:
        pass
    te = ''
    for part in team:
        te = te + part+'\n'

    combine = [name, symbol, country, raised, startdate, enddate,
               platform, type, amount, accept, distri, soft, hard, bonus, te, socials]
    print(combine)
    outfile.write(str(combine))
    outfile.write('\n')
    outfile.flush()


    browser.quit()