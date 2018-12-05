import pandas as pd
import os

p = pd.read_csv('/users/barry/desktop/ico_output.csv', encoding = "ISO-8859-1")


wp = p.to_dict(orient="list")

for i in range(len(wp['Name'])):
    if str(wp['end_time'][i]) != 'nan':
        continue
    elif str(wp['Enddate(tm)'][i]) != 'nan':
        wp['end_time'][i] = wp['Enddate(tm)'][i]
    elif str(wp['Enddate(cryptocompare)'][i]) != 'nan' :
        wp['end_time'][i] = wp['Enddate(cryptocompare)'][i]
    elif str(wp['End(ICOmarks)'][i]) != 'nan':
        wp['end_time'][i] = wp['End(ICOmarks)'][i]
    elif str(wp['Enddate(ICOdrops)'][i]) != 'nan':
        wp['end_time'][i] = wp['Enddate(ICOdrops)'][i]
    elif str(wp['End_date(icobench)'][i]) != 'nan':
        wp['end_time'][i] = wp['End_date(icobench)'][i]


ddd = pd.DataFrame(wp)
ddd.to_csv('/users/barry/desktop/www.csv')
