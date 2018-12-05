from selenium import webdriver
import pandas as pd

dic = {'name':[], 't.me':[], 'medium':[], 'facebook':[], 'twitter':[], 'bitcointalk':[], 'linkedin':[],
       'instagram':[], 'youtube':[], 'reddit':[], 'discord':[], 'github':[], 'slack':[], 'chat':[], 'google':[]}


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
            d = {'name':'NA', 't.me':'NA', 'medium':'NA', 'facebook':'NA', 'twitter':'NA', 'bitcointalk':'NA', 'linkedin':'NA', 'instagram':'NA',
                 'youtube':'NA', 'reddit':'NA', 'discord':'NA', 'github':'NA', 'slack':'NA', 'chat':'NA', 'google':'NA'}
            browser.get(url)
            browser.implicitly_wait(3)
            d['name'] = browser.find_element_by_class_name('ico-main-info').text.split('\n')[0]
            if d['name'] not in index_name:
                print(d['name'], 'not in ')
                continue
            print(d['name'])
            links = browser.find_element_by_class_name('soc_links').find_elements_by_tag_name('a')
            for link in links:
                l = link.get_attribute('href')
                for index in d:
                    if index in l:
                        d[index] = l
                        break
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
    #ico_list = ['https://icodrops.com/gems/', 'https://icodrops.com/arcblock/' ]
    name_index = pd.read_csv('/users/barry/desktop/ico_index.csv')
    index_name = name_index['name'].values
    print(len(ico_list))
    dictionary = get_info(ico_list)
    print(dictionary)
    ddd = pd.DataFrame(dictionary)

    ddd.to_csv('/users/barry/desktop/ex2.csv')