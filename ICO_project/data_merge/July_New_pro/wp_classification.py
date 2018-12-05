import pandas as pd
import os
import shutil

def classify(amount):
    if str(amount) == 'nan':
        return '/users/barry/desktop/wp/no-data'
    elif int(amount) >= 100000000:
        return '/users/barry/desktop/wp/100m'
    elif int(amount) >= 10000000:
        return '/users/barry/desktop/wp/10m'
    elif int(amount) >= 1000000:
        return '/users/barry/desktop/wp/1m'
    else:
        return '/users/barry/desktop/wp/no-m'

path_wp = '/users/barry/desktop/whitepapers'
files =os.listdir(path_wp)



b = pd.read_csv('/users/barry/desktop/work.csv', encoding = "ISO-8859-1")

for i in range(len(b['Name'])):
    name = b['Name'][i]
    for file in files:
        if file == (name+'.pdf'):
            srcfile = os.path.join(path_wp, file)
            path = classify(b['raised_money'][i])
            targetfile = os.path.join(path, file)
            shutil.copyfile(srcfile, targetfile)
            break