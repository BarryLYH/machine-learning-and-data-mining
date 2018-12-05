import pandas as pd
import os

p = pd.read_csv('/users/barry/desktop/wp&raised.csv', encoding = "ISO-8859-1")

wp = p.to_dict(orient="list")

path = '/users/barry/desktop/whitepapers'
files =os.listdir(path)

for file in files:
    name = file[:-4]
    for i in range(len(wp['Name'])):
        if name == wp['Name'][i]:
            wp["Downloaded"][i] = 1
            break

for i in range(len(wp['Name'])):
    if wp['Downloaded'][i] != 1:
        wp["Downloaded"][i] = 0


ddd = pd.DataFrame(wp)

ddd.to_csv('/users/barry/desktop/wpraised.csv')
