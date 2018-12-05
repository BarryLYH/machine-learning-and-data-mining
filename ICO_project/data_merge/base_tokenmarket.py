import pandas as pd


def sameone(i, j):
    if str(toma['Name'][i]).lower() == str(base['name'][j]).lower() or toma['Website'][i] == base['weblink'][j]:
        return True

    return False



b = pd.read_csv('/users/barry/desktop/BASE.csv')
t= pd.read_csv('/users/barry/desktop/tokenmarket.csv', encoding = "ISO-8859-1")

base = b.to_dict(orient="list")
toma = t.to_dict(orient="list")

for i in range(len(toma['Name'])):
    exist = 0
    for j in range(len(base['name'])):
        if sameone(i, j):
            exist = 1
            for index in toma:
                if index + '(tm)' in base:
                    base[index+'(tm)'][j] = toma[index][i]
            break

    if exist == 0:
        for index in base:
            base[index].append('NA')
        l = len(base['name']) - 1
        base['name'][l] = toma['Name'][i]
        for index in toma:
            if index+'(tm)' in base:
                base[index+'(tm)'][l] = toma[index][i]
    print(len(base['name']))

ddd = pd.DataFrame(base)
ddd = ddd[['name', 'symbol', 'Failed/Completed', 'raised_money', 'WP', 'Github',
       'start_time', 'end_time', 'weblink', 'Symbol(tm)', 'Country(tm)',
       'Startdate(tm)', 'Enddate(tm)', 'Concept(tm)', 'Website(tm)',
       'Whitepaper(tm)', 'Blog(tm)', 'Facebook(tm)', 'Github(tm)',
       'Linkedin(tm)', 'Slack chat(tm)', 'Telegram chat(tm)', 'Twitter(tm)']]
ddd.to_csv('/users/barry/desktop/base1.csv')





