import pandas as pd

infile = open('/users/barry/Desktop/icobench_data2.txt', 'r')
lines = infile.readlines()
infile.close()

base = {'Name':[], 'Symbol':[], 'Country':[], 'Raise_money':[], 'Start_date':[],
        'End_date': [], 'Platform':[], 'Type':[], 'Token_amount':[], 'Accept':[],
        'Distribution': [], 'soft_cap':[], 'hard_cap':[], 'Bonus':[], 'Team':[], 'Social_links':[]}

for line in lines:
    line = line.replace('\"', '\'')
    elements = line[2:-3].split('\', \'')
    if len(elements) < 16:
        print(elements)
    base['Name'].append(elements[0])
    base['Symbol'].append(elements[1])
    base['Country'].append(elements[2])
    base['Raise_money'].append(elements[3])
    base['Start_date'].append(elements[4])
    base['End_date'].append(elements[5])
    base['Platform'].append(elements[6])
    base['Type'].append(elements[7])
    base['Token_amount'].append(elements[8])
    base['Accept'].append(elements[9])
    base['Distribution'].append(elements[10])
    base['soft_cap'].append(elements[11])
    base['hard_cap'].append(elements[12])
    base['Bonus'].append(elements[13])
    if len(elements) == 14:
        base['Team'].append("NA")
        base['Social_links'].append("NA")
    elif len(elements) == 15:
        if elements[14][:4] == 'Team':
            base['Team'].append(elements[14])
        else:
            base['Social_links'].append(elements[14])
    elif len(elements) == 16:
        base['Team'].append(elements[14])
        base['Social_links'].append(elements[15])

ddd = pd.DataFrame(base)
ddd.to_csv('/users/barry/desktop/basss.csv')


