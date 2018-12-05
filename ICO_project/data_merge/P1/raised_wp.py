import pandas as pd
import os

p = pd.read_csv('/users/barry/desktop/Project 1/project1_wp_links.csv', encoding = "ISO-8859-1")
b = pd.read_csv('/users/barry/desktop/Project 1/project1_content.csv', encoding = "ISO-8859-1")

rm = b.to_dict(orient='list')
wp = p.to_dict(orient="list")

result = {"Name":[]}

counter = 0
counter1 = 0

for i in range(len(wp['Name'])):
    if str(rm['Raised_money (USD)'][i])!='nan' or str(rm['Raised_money_ICOmarks (USD)'][i])!= 'nan'\
            or str(rm['Raised_money_cryptocompare (USD)'][i])!='nan'\
            or str(rm['Raised_money_ICOdrops (USD)'][i]) != 'nan':
        counter1 += 1
        if wp['Downloaded'][i] == 0:
            result['Name'].append(str(rm['Name'][i]))
            counter += 1
print(counter)
print(counter1)

ddd = pd.DataFrame(result)
ddd.to_csv('/users/barry/desktop/miss.csv')