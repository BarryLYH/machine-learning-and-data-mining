import pandas as pd



def sameone(i, j):
    if str(toma['Name'][i]).lower() == str(base['name'][j]).lower() or toma['Website'][i] == base['weblink'][j]:
        return True
    if toma['Website'][i] == base['Website(tm)'][j] or toma['Website'][i] == base['Website(ICOmarks)'][j]:
        return True
    return False



b = pd.read_csv('/users/barry/desktop/base2.csv', encoding = "ISO-8859-1")
t= pd.read_csv('/users/barry/desktop/coinmarketcap_content.csv', encoding = "ISO-8859-1")

base = b.to_dict(orient="list")
toma = t.to_dict(orient="list")


counter = 0
for i in range(len(toma['Name'])):
    exist = 0
    for j in range(len(base['name'])):
        if sameone(i, j):
            exist = 1
            for index in toma:
                if index + '(coinmarketcap)' in base:
                    base[index+'(coinmarketcap)'][j] = toma[index][i]
            break

    if exist == 0:
        counter += 1
        for index in base:
            base[index].append('NA')
        l = len(base['name']) - 1
        base['name'][l] = toma['Name'][i]
        for index in toma:
            if index+'(coinmarketcap)' in base:
                base[index+'(coinmarketcap)'][l] = toma[index][i]
    print(len(base['name']))


print(counter)
ddd = pd.DataFrame(base)
ddd = ddd[['name', 'symbol', 'Failed/Completed', 'raised_money', 'WP', 'Github',
       'start_time', 'end_time', 'weblink', 'Symbol(tm)', 'Country(tm)',
       'Startdate(tm)', 'Enddate(tm)', 'Concept(tm)', 'Website(tm)',
       'Whitepaper(tm)', 'Blog(tm)', 'Facebook(tm)', 'Github(tm)',
       'Linkedin(tm)', 'Slack chat(tm)', 'Telegram chat(tm)', 'Twitter(tm)',
       'Symbol(ICOmarks)', 'Start(ICOmarks)', 'End(ICOmarks)',
       'Pre-Start(ICOmarks)', 'Pre-End(ICOmarks)', 'Raised(ICOmarks)',
       'Website(ICOmarks)', 'Accepting(ICOmarks)', 'Bitcointalk(ICOmarks)',
       'Bounty(ICOmarks)', 'Country(ICOmarks)', 'Facebook(ICOmarks)',
       'Github(ICOmarks)', 'Linkedin(ICOmarks)', 'Medium(ICOmarks)',
       'Platform(ICOmarks)', 'Price(ICOmarks)', 'Reddit(ICOmarks)',
       'Slack(ICOmarks)', 'Telegram(ICOmarks)', 'Token Type(ICOmarks)',
       'Twitter(ICOmarks)', 'Whitepaper(ICOmarks)', 'Symbol(coinmarketcap)',
       'Announcement(coinmarketcap)', 'Chat(coinmarketcap)',
       'Chat 2(coinmarketcap)', 'Circulating Supply(coinmarketcap)',
       'Explorer(coinmarketcap)', 'Explorer 2(coinmarketcap)',
       'Explorer 3(coinmarketcap)', 'Max Supply(coinmarketcap)',
       'Message Board(coinmarketcap)', 'Message Board 2(coinmarketcap)',
       'Message Board 3(coinmarketcap)', 'Source Code(coinmarketcap)',
       'Website(coinmarketcap)', 'Website 2(coinmarketcap)']]

ddd.to_csv('/users/barry/desktop/base3.csv')





