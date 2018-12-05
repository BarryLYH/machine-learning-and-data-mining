import pandas as pd
import urllib.request
import re
import os

def getFile(target_url, file_name):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
    req = urllib.request.Request(url=target_url, headers=headers)
    u = urllib.request.urlopen(req, timeout = 30)
    f = open(file_name, 'wb')
    block_sz = 8192
    while True:
        buffer = u.read(block_sz)
        if not buffer:
            break

        f.write(buffer)
    f.close()
    print ("Sucessful to download" + " " + file_name)

p= pd.read_csv('/users/barry/desktop/wpra.csv', encoding = "ISO-8859-1")
wp = p.to_dict(orient="list")


os.mkdir('/users/barry/desktop/pdf_download')
os.chdir(os.path.join(os.getcwd(), '/users/barry/desktop/pdf_download'))

for i in range(len(wp['Name'])):
    if wp['Downloaded'][i] == 0:
        print(wp['Name'][i])
        links = []
        if str(wp['Whitepaper(ICOdrops)'][i]) != 'nan': links.append(wp['Whitepaper(ICOdrops)'][i])
        if str(wp['Whitepaper(ICOmarks)'][i]) != 'nan': links.append(wp['Whitepaper(ICOmarks)'][i])
        if str(wp['Whitepaper(icobench)'][i]) != 'nan': links.append(wp['Whitepaper(icobench)'][i])
        if str(wp['Whitepaper(tm)'][i]) != 'nan': links.append(wp['Whitepaper(tm)'][i])
        if len(links) > 0:
            Judge = True
            j = 0
            while Judge and j<len(links):
                print(links)
                url = links[j]
                j+=1
                file_name = wp['Name'][i]+'.pdf'
                try:
                    getFile(url, file_name)
                    wp['Downloaded'][i] = 1
                    Judge =False
                except:
                    continue

ddd = pd.DataFrame(wp)
ddd = ddd[['Name', 'Downloaded', 'Whitepaper(ICOdrops)', 'Whitepaper(ICOmarks)', 'Whitepaper(icobench)', 'Whitepaper(tm)',
           'raised_money', 'Raised(ICOmarks)', 'Raised(cryptocompare)', 'Raised_money(ICOdrops)', 'Raised_money(icobench)']]
ddd.to_csv('/users/barry/desktop/project1_wp_links1.csv')

