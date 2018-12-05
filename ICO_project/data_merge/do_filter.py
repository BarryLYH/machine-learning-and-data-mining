import pandas as pd

def combine(i,j):
    for index in base:
        if str(base[index][j]) != 'nan' and index != 'name':
            base[index][i] = base[index][j]


b = pd.read_csv('/users/barry/desktop/base_raw2.csv', encoding = "ISO-8859-1")

base = b.to_dict(orient="list")

infile = open('/users/barry/Desktop/filter2.txt', 'r')
lines = infile.readlines()
infile.close()

length = len(base['name'])
list = []
for line in lines:
    line = line.strip('\n')
    names = line.split('  ----  ')
    for i in range(length):
        if base['name'][i] == names[0]:
            for j in range(i+1, length):
                if base['name'][j] == names[1]:
                    print(base['name'][j])
                    list.append(base['name'][j])
                    combine(i,j)
print(len(list))

i = 0
while i< length:
    if base['name'][i] in list:
        for index in base:
            base[index].pop(i)
        i -= 1
    i += 1
    length = len(base['name'])

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
       'Website(coinmarketcap)', 'Website 2(coinmarketcap)',
       'Symbol(cryptocompare)', 'Raised(cryptocompare)',
       'Startdate(cryptocompare)', 'Enddate(cryptocompare)',
       'Accepting(cryptocompare)', 'Algorithm(cryptocompare)',
       'Prooftype(cryptocompare)', 'TokenSupply(cryptocompare)',
       'TokenType(cryptocompare)', 'raised_amount_usd(ICOdrops)',
       'start_date(ICOdrops)', 'end_date(ICOdrops)', 'Website(ICOdrops)',
       'bitcointalk(ICOdrops)', 'chat(ICOdrops)', 'discord(ICOdrops)',
       'facebook(ICOdrops)', 'github(ICOdrops)', 'google(ICOdrops)',
       'instagram(ICOdrops)', 'linkedin(ICOdrops)', 'medium(ICOdrops)',
       'reddit(ICOdrops)', 'slack(ICOdrops)', 't.me(ICOdrops)',
       'twitter(ICOdrops)', 'youtube(ICOdrops)']]

ddd.to_csv('/users/barry/desktop/base_raw2.csv')