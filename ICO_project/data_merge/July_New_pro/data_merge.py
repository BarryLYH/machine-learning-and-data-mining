import pandas as pd



def sameone(i, j):
    if str(toma['Name'][i]).lower() == str(base['name'][j]).lower() or toma['Website'][i] == base['weblink'][j]:
        return True
    if toma['Website'][i][:-21] == base['Website(tm)'][j] or toma['Website'][i][:-21] == base['Website(ICOdrops)'][j]:
        return True
    if toma['Website'][i][:-21] == base['Website(ICOmarks)'][j] or toma['Website'][i][:-21] == base['Website(coinmarketcap)'][j]:
        return True
    if toma['Website'][i][:-21] == base['Website(ICOmarks)'][j] or toma['Website'][i][:-21] == base['Website(coinmarketcap)'][j]:
        return True
    if toma['Github'][i] == base['Github(tm)'][j] or toma['Facebook'][i] == base['Facebook(tm)'][j]:
        return True
    if toma['Github'][i] == base['Github(coinmarketcap)'][j] or toma['Github'][i] == base['github(ICOdrops)'][j]:
        return True
    if toma['Twitter'][i] == base['Twitter(tm)'][j] or toma['Twitter'][i] == base['Twitter(ICOmarks)'][j]:
        return True
    if toma['Twitter'][i] == base['twitter(ICOdrops)'][j] or toma['Facebook'][i] == base['Facebook(ICOmarks)'][j]:
        return True
    return False



b = pd.read_csv('/users/barry/desktop/base.csv', encoding = "ISO-8859-1")
t= pd.read_csv('/users/barry/desktop/icobench_2.csv', encoding = "ISO-8859-1")

base = b.to_dict(orient="list")
toma = t.to_dict(orient="list")


counter = 0
for i in range(len(toma['Name'])):
    exist = 0
    for j in range(len(base['name'])):
        if sameone(i, j):
            exist = 1
            for index in toma:
                if index + '(icobench)' in base:
                    base[index+'(icobench)'][j] = toma[index][i]
            break

    if exist == 0:
        counter += 1
        for index in base:
            base[index].append('NA')
        l = len(base['name']) - 1
        base['name'][l] = toma['Name'][i]
        for index in toma:
            if index+'(icobench)' in base:
                base[index+'(icobench)'][l] = toma[index][i]
    print(len(base['name']))


print(counter)
ddd = pd.DataFrame(base)
ddd = ddd[['name', 'Background', 'symbol', 'Symbol(tm)', 'Symbol(ICOmarks)', 'Symbol(cryptocompare)',
           'Symbol(coinmarketcap)', 'Symbol(ICOdrops)', 'Concept(tm)', 'Country(tm)', 'Country(ICOmarks)',
           'Output', 'raised_money', 'Raised_money(ICOdrops)', 'Raised(cryptocompare)', 'Raised(ICOmarks)', 'Tech',
           'Token type(ICOdrops)', 'TokenSupply(cryptocompare)', 'TokenType(cryptocompare)',
           'Circulating Supply(coinmarketcap)', 'Algorithm(cryptocompare)', 'Prooftype(cryptocompare)', 'Platform(ICOmarks)',
           'Marketing', 'start_time', 'end_time', 'Startdate(tm)', 'Enddate(tm)', 'Startdate(cryptocompare)',
           'Enddate(cryptocompare)', 'Start(ICOmarks)', 'End(ICOmarks)', 'Startdate(ICOdrops)', 'Enddate(ICOdrops)',
           'Target(ICOdrops)', 'Sold on pre-sale(ICOdrops)', 'Total Tokens(ICOdrops)', 'Available for Token Sale(ICOdrops)',
           'Accepts(ICOdrops)', 'Accepting(ICOmarks)', 'Price(ICOmarks)', 'StartPrice(cryptocompare)',
           'StartPriceCurrency(cryptocompare)', 'Bonus for the First(ICOdrops)', 'SecurityAuditCompany(cryptocompare)',
           'Min/Max Personal Cap(ICOdrops)', 'Bounty(ICOmarks)', 'Whitelist(ICOdrops)', 'Know Your Customer (KYC)(ICOdrops)',
           'Token Issue(ICOdrops)', 'Community', 'weblink', 'Website(tm)', 'Whitepaper(tm)', 'Blog(tm)', 'Facebook(tm)',
           'Github(tm)', 'Linkedin(tm)', 'Slack chat(tm)', 'Telegram chat(tm)', 'Twitter(tm)', 'Announcement(coinmarketcap)',
           'Chat(coinmarketcap)', 'Chat 2(coinmarketcap)', 'Explorer(coinmarketcap)', 'Explorer 2(coinmarketcap)',
           'Explorer 3(coinmarketcap)', 'Max Supply(coinmarketcap)', 'Message Board(coinmarketcap)',
           'Message Board 2(coinmarketcap)', 'Message Board 3(coinmarketcap)', 'Github(coinmarketcap)', 'Website(coinmarketcap)',
           'Website 2(coinmarketcap)', 'Website(ICOmarks)', 'Facebook(ICOmarks)', 'Github(ICOmarks)', 'Linkedin(ICOmarks)',
           'Medium(ICOmarks)', 'Bitcointalk(ICOmarks)', 'Reddit(ICOmarks)', 'Slack(ICOmarks)', 'Telegram(ICOmarks)', 'Token Type(ICOmarks)',
           'Twitter(ICOmarks)', 'Whitepaper(ICOmarks)', 'Website(ICOdrops)', 'Whitepaper(ICOdrops)', 'ICO Token Price(ICOdrops)',
           'bitcointalk(ICOdrops)', 'chat(ICOdrops)', 'discord(ICOdrops)', 'facebook(ICOdrops)', 'github(ICOdrops)', 'google(ICOdrops)',
           'instagram(ICOdrops)', 'linkedin(ICOdrops)', 'medium(ICOdrops)', 'reddit(ICOdrops)', 'slack(ICOdrops)', 't.me(ICOdrops)',
           'twitter(ICOdrops)', 'youtube(ICOdrops)', 'Others', 'Failed/Completed(tm)', 'Pre-Start(ICOmarks)', 'Pre-End(ICOmarks)',
           'Symbol(icobench)', 'Country(icobench)', 'Raised_money(icobench)', 'Token_amount(icobench)', 'Start_date(icobench)',
           'End_date(icobench)', 'ICO_distribution(icobench)', 'Token_price(icobench)', 'Accept(icobench)', 'Bonus(icobench)',
           'Platform(icobench)', 'Team(icobench)', 'Token_type(icobench)', 'hard_cap(icobench)', 'soft_cap(icobench)', 'Website(icobench)',
           'Whitepaper(icobench)', 'Bitcointalk(icobench)', 'Blog(icobench)', 'Discord(icobench)', 'Facebook(icobench)', 'Github(icobench)',
           'Medium(icobench)', 'Reddit(icobench)', 'Slack(icobench)', 'Telegram(icobench)', 'Twitter(icobench)', 'VK(icobench)']]

ddd.to_csv('/users/barry/desktop/base7.csv')





