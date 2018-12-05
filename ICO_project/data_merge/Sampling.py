import pandas as pd
import os

p = pd.read_csv('/users/barry/desktop/wpraised.csv', encoding = "ISO-8859-1")


wp = p.to_dict(orient="list")

for i in range(len(wp['Name'])):
    if str(wp['raised_money'][i]) != 'nan':
        continue
    elif str(wp['Raised_money(ICOdrops)'][i]) != 'nan':
        wp['raised_money'][i] = wp['Raised_money(ICOdrops)'][i]
    elif str(wp['Raised(cryptocompare)'][i]) != 'nan':
        wp['raised_money'][i] = wp['Raised(cryptocompare)'][i]
    elif str(wp['Raised(ICOmarks)'][i]) != 'nan':
        wp['raised_money'][i] = wp['Raised(ICOmarks)'][i]
    elif str(wp['Raised_money(icobench)'][i]) != 'nan' and str(wp['Raised_money(icobench)'][i]) != 'Unknown':
        wp['raised_money'][i] = wp['Raised_money(icobench)'][i]

ddd = pd.DataFrame(wp)
ddd.to_csv('/users/barry/desktop/wr.csv')
