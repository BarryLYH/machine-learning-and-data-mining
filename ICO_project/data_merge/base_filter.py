import pandas as pd

def judgement(i,j):
    list1 = []
    if str(base['symbol'][i]) != 'nan': list1.append(base['symbol'][i])
    if str(base['Symbol(tm)'][i]) != 'nan': list1.append(base['Symbol(tm)'][i])
    if str(base['Symbol(ICOmarks)'][i]) != 'nan': list1.append(base['Symbol(ICOmarks)'][i])
    if str(base['Symbol(coinmarketcap)'][i]) != 'nan': list1.append(base['Symbol(coinmarketcap)'][i])
    if str(base['Symbol(cryptocompare)'][i]) != 'nan': list1.append(base['Symbol(cryptocompare)'][i])
    list2 = []
    if str(base['symbol'][j]) != 'nan': list2.append(base['symbol'][j])
    if str(base['Symbol(tm)'][j]) != 'nan': list2.append(base['Symbol(tm)'][j])
    if str(base['Symbol(ICOmarks)'][j]) != 'nan': list2.append(base['Symbol(ICOmarks)'][j])
    if str(base['Symbol(coinmarketcap)'][j]) != 'nan': list2.append(base['Symbol(coinmarketcap)'][j])
    if str(base['Symbol(cryptocompare)'][j]) != 'nan': list2.append(base['Symbol(cryptocompare)'][j])
    for part1 in list1:
        for part2 in list2:
            if part1 == part2:
                return True
    return False

b = pd.read_csv('/users/barry/desktop/base_raw2.csv', encoding = "ISO-8859-1")

base = b.to_dict(orient="list")

filter = []

for i in range(len(base['name'])):
    for j in range(i+1, len(base['name'])):
        if judgement(i,j):
            filter.append(base['name'][i]+'  ----  '+base['name'][j])

outfile = open('/users/barry/Desktop/filter2.txt', 'w')


counter = 0
for part in filter:
    counter += 1
    outfile.write(part+'\n')
outfile.close()
print(counter)