import pandas as pd


b = pd.read_csv('/users/barry/desktop/wp_rm.csv', encoding = "ISO-8859-1")

base = b.to_dict(orient="list")

wp = {'Name': [], 'Whitepaper_link1': [], 'Whitepaper_link2': []}

for i in range(len(base['name'])):
    wp["Name"].append(base['name'][i])
    wp['Whitepaper_link1'].append(base['Whitepaper(tm)'][i])
    wp['Whitepaper_link2'].append(base['Whitepaper(ICOmarks)'][i])

for i in range(len(wp['Name'])):
if str(wp['Whitepaper_link1'][i]) != 'nan':
    wp['Whitepaper_link'][i] = wp['Whitepaper_link1'][i]
else:
    wp['Whitepaper_link'][i] = wp['Whitepaper_link2'][i]

ddd = pd.DataFrame(wp)
ddd.to_csv('/users/barry/desktop/wp.csv')