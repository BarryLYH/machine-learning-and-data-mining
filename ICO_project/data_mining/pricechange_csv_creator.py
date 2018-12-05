import os
import pandas as pd

dic = {'Name':[], 'Date':[], 'Open':[],'High':[],
       'Low':[],'Close':[],'Volume':[],'MarketCap':[]}

path = '/users/barry/desktop/cmc_price'
files = os.listdir(path)

counter = 0
for file in files:
    if file[-3:] == 'txt':
        counter += 1
        print(counter, file)
        name = file[:-4]
        infile = open(path+'/'+file,'r')
        lines = infile.readlines()
        infile.close()
        for line in lines:
            dic['Name'].append(name)
            data = line.strip('\n').split(' ')
            dic['Date'].append(data[0])
            dic['Open'].append(data[1])
            dic['High'].append(data[2])
            dic['Low'].append(data[3])
            dic['Close'].append(data[4])
            dic['Volume'].append(data[5])
            dic['MarketCap'].append(data[6])

ddd = pd.DataFrame(dic)

ddd.to_csv('/users/barry/desktop/coinmarketcap_price.csv')




