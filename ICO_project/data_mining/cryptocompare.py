from selenium import webdriver
import pandas as pd
import time

databasedic = {'Name':[], 'Symbol':[], 'Startdate':[], 'Enddate':[], 'Raised':[],
             'TokenSupply':[], 'Prooftype':[], 'Algorithm':[],
                'TokenType':[], 'StartPrice':[], 'StartPriceCurrency':[],
               'SecurityAuditCompany':[]}

def processed(element):
    return element.split('\"')[1]

def timetransfer(date):
    x = time.localtime(int(date))
    return time.strftime('%Y-%m-%d',x)

infile = open('/users/barry/Desktop/compara.txt', 'r')
#infile = open('/users/barry/Desktop/11.txt', 'r')
total_data = infile.read()
infile.close()

data = total_data.split('},\n')
for part in data:
    databasein = {'Name':' ', 'Symbol':' ', 'Startdate':' ', 'Enddate':' ', 'Raised':' ',
                   'TokenSupply':' ', 'Prooftype':' ',
                  'Algorithm':' ', 'TokenType':' ','StartPrice':' ', 'StartPriceCurrency':' ',
               'SecurityAuditCompany':'NA'}
    datalines = part.split('\n')
    datalines = datalines[:-1]
    for l in datalines:
        front_ele = processed(l.split(': ')[0])
        try:
            end_ele = processed(l.split(': ')[1])
        except:
            if front_ele == 'ICODate':
                tim = timetransfer(l.split(': ')[1][:-1])
                if tim == '1969-12-31':
                 databasein['Startdate'] = ' '
                else:
                 databasein['Startdate'] = timetransfer(l.split(': ')[1][:-1])
            elif front_ele == 'ICOEndDate':
                tim = timetransfer(l.split(': ')[1][:-1])
                if tim == '1969-12-31':
                    databasein['Enddate'] = ' '
                else:
                    databasein['Enddate'] = timetransfer(l.split(': ')[1][:-1])
            continue
        if front_ele == 'FullName':
            databasein['Name'] = end_ele.split(' (')[0]
        elif front_ele == 'Name':
            if end_ele == '-' or end_ele =='N/A':
                databasein['Symbol'] = ' '
            else:
                databasein['Symbol'] = end_ele
        elif front_ele == 'ICOFundsRaisedUSD':
            if end_ele == '-' or end_ele =='N/A':
                databasein['Raised'] = ' '
            else:
                databasein['Raised'] = end_ele
        elif front_ele == 'ProofType':
            if end_ele == '-' or end_ele =='N/A':
                databasein['Prooftype'] = ' '
            else:
                databasein['Prooftype'] = end_ele
        elif front_ele == 'Algorithm':
            if end_ele == '-' or end_ele =='N/A':
                databasein['Algorithm'] = ' '
            else:
                databasein['Algorithm'] = end_ele
        elif front_ele == 'ICOTokenType':
            if end_ele == '-' or end_ele =='N/A':
                databasein['TokenType'] = ' '
            else:
                databasein['TokenType'] = end_ele
        elif front_ele == 'ICOTokenSupply':
            if end_ele == '-' or end_ele =='N/A':
                databasein['TokenSupply'] = ' '
            else:
                databasein['TokenSupply']= end_ele
        elif front_ele == 'ICOStartPrice':
            if end_ele == '-' or end_ele =='N/A':
                databasein['StartPrice'] = ' '
            else:
                databasein['StartPrice'] = end_ele
        elif front_ele == 'ICOStartPriceCurrency':
            if end_ele == '-' or end_ele =='N/A':
                databasein['StartPriceCurrency'] = ' '
            else:
                databasein['StartPriceCurrency'] = end_ele
        elif front_ele == 'ICOSecurityAuditCompany':
            if end_ele == '-' or end_ele =='N/A':
                databasein['SecurityAuditCompany'] = ' '
            else:
                databasein['SecurityAuditCompany'] = end_ele

    for index in databasein:
        databasedic[index].append(databasein[index])
    print(databasein)
ddd = pd.DataFrame(databasedic)
ddd = ddd[['Name', 'Symbol', 'Startdate', 'Enddate', 'Raised',
                'TokenSupply', 'Prooftype', 'Algorithm',
                'TokenType', 'StartPrice', 'StartPriceCurrency',
               'SecurityAuditCompany']]
ddd.to_csv('/users/barry/desktop/cryptocompare.csv')