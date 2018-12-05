import pandas as pd


b = pd.read_csv('/users/barry/desktop/base_new.csv', encoding = "ISO-8859-1")

bb = {'name':[], 'Whitepaper(tm)':[], 'Whitepaper(ICOmarks)':[], 'Whitepaper(ICOdrops)':[], 'Whitepaper(icobench)':[],
     'raised_money':[], 'Raised_money(ICOdrops)':[], 'Raised(cryptocompare)':[], 'Raised(ICOmarks)':[], 'Raised_money(icobench)':[]}

for i in range(len(b['name'])):
     for index in bb:
          bb[index].append(b[index][i])

ddd = pd.DataFrame(bb)
ddd = ddd[['name', 'Whitepaper(ICOdrops)', 'Whitepaper(ICOmarks)', 'Whitepaper(icobench)', 'Whitepaper(tm)',
           'raised_money', 'Raised(ICOmarks)', 'Raised(cryptocompare)', 'Raised_money(ICOdrops)', 'Raised_money(icobench)']]
ddd.to_csv('/users/barry/desktop/wp&raised.csv')