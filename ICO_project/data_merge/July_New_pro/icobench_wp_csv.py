import pandas as pd

d = {'Name':[], 'Website':[], 'Token_price':[]}

infile = open('/users/barry/Desktop/data2.txt', 'r')
links = infile.readlines()
infile.close()


for line in links:
    dd = {'Name': 'NA', 'Website': 'NA', 'Token_price': 'NA'}
    line = line.strip('\n')
    print(line)
    contents = line.split('++++')
    print(contents)
    d['Name'].append(contents[0])
    d['Website'].append(contents[1])
    d['Token_price'].append(contents[2])


ddd = pd.DataFrame(d)
ddd.to_csv('/users/barry/desktop/baaaa.csv')