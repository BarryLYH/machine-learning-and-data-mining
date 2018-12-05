import pandas as pd

b = pd.read_csv('/users/barry/desktop/wp&raised.csv', encoding = "ISO-8859-1")

list=[]
for index in b:
    list.append(index)
print(list)