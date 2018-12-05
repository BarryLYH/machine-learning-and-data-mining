import pandas as pd


b = pd.read_csv('/users/barry/desktop/base.csv', encoding = "ISO-8859-1")
p = pd.read_csv('/users/barry/desktop//project1_content.csv', encoding = "ISO-8859-1")

base = b.to_dict(orient="list")
p1 = p.to_dict(orient='list')

for i in range(len(base['name'])):

    p1['Name'].append(base['name'][i])
    p1['Start_date'].append(base['start_time'][i])
    p1['End_date'].append(base['end_time'][i])
    p1['Start_date_tokenmarket'].append(base['Startdate(tm)'][i])
    p1['End_date_tokenmarket'].append(base['Enddate(tm)'][i])
    p1['Start_date_ICOmarks'].append(base['Start(ICOmarks)'][i])
    p1['End_date_ICOmarks'].append(base['End(ICOmarks)'][i])
    p1['Start_date_cryptocompare'].append(base['Startdate(cryptocompare)'][i])
    p1['End_date_cryptocompare'].append(base['Enddate(cryptocompare)'][i])
    p1['Start_date_ICOdrops'].append(base['Startdate(ICOdrops)'][i])
    p1['End_date_ICOdrops'].append(base['Enddate(ICOdrops)'][i])
    p1['Raised_money (USD)'].append(base['raised_money'][i])
    p1['Raised_money_ICOmarks (USD)'].append(base['Raised(ICOmarks)'][i])
    p1['Raised_money_cryptocompare (USD)'].append(base['Raised(cryptocompare)'][i])
    p1['Raised_money_ICOdrops (USD)'].append(base['Raised_money(ICOdrops)'][i])
    if str(base['Github'][i])!='nan' or str(base['Github(tm)'][i])!='nan' or str(base['Github(ICOmarks)'][i])!='nan'\
        or str(base['Source Code(coinmarketcap)'][i])!='nan' or str(base['github(ICOdrops)'][i])!='nan':
        p1['Github'].append(1)
    else:
        p1['Github'].append(0)
    if str(base['Facebook(tm)'][i])!='nan' or str(base['Facebook(ICOmarks)'][i])!='nan' or str(base['facebook(ICOdrops)'][i])!='nan':
        p1['Facebook'].append(1)
    else:
        p1['Facebook'].append(0)
    if str(base['Linkedin(tm)'][i])!='nan' or str(base['Linkedin(ICOmarks)'][i])!='nan' or str(base['linkedin(ICOdrops)'][i])!='nan':
        p1['Linkedin'].append(1)
    else:
        p1['Linkedin'].append(0)
    if str(base['Telegram chat(tm)'][i])!='nan' or str(base['Telegram(ICOmarks)'][i])!='nan' or str(base['t.me(ICOdrops)'][i])!='nan':
        p1['Telegram'].append(1)
    else:
        p1['Telegram'].append(0)
    if str(base['Twitter(tm)'][i])!='nan' or str(base['Twitter(ICOmarks)'][i])!='nan' or str(base['twitter(ICOdrops)'][i])!='nan':
        p1['Twitter'].append(1)
    else:
        p1['Twitter'].append(0)
    if str(base['Reddit(ICOmarks)'][i])!='nan' or str(base['reddit(ICOdrops)'][i])!='nan':
        p1['Reddit'].append(1)
    else:
        p1['Reddit'].append(0)
    if str(base['medium(ICOdrops)'][i])!='nan' or str(base['Medium(ICOmarks)'][i])!='nan':
        p1['Medium'].append(1)
    else:
        p1['Medium'].append(0)


    if str(base['Failed/Completed'][i])=='0.0':
        p1['Failure'].append(0)
    else:
        p1['Failure'].append('Waiting')


    if str(base['symbol'][i])!='nan' or str(base['Failed/Completed'][i])!='nan' or str(base['raised_money'][i])!='nan'\
            or str(base['weblink'][i])!='nan' or str(base['start_time'][i])!='nan':
        p1['Tokendata'].append(1)
    else:
        p1['Tokendata'].append(0)
    if str(base['Symbol(tm)'][i])!='nan' or str(base['Startdate(tm)'][i])!='nan' or str(base['Website(tm)'][i])!='nan'\
            or str(base['Concept(tm)'][i])!='nan' or str(base['Whitepaper(tm)'][i])!='nan':
        p1['Tokenmarket'].append(1)
    else:
        p1['Tokenmarket'].append(0)
    if str(base['Symbol(coinmarketcap)'][i])!='nan' or str(base['Announcement(coinmarketcap)'][i])!='nan'\
            or str(base['Circulating Supply(coinmarketcap)'][i])!='nan' or str(base['Message Board(coinmarketcap)'][i])!='nan':
        p1['Coinmarketcap'].append(1)
    else:
        p1['Coinmarketcap'].append(0)
    if str(base['Symbol(ICOmarks)'][i])!='nan' or str(base['Website(ICOmarks)'][i])!='nan' or str(base['Start(ICOmarks)'][i])!='nan'\
            or str(base['Raised(ICOmarks)'][i])!='nan' or str(base['Whitepaper(ICOmarks)'][i])!='nan':
        p1['ICOmarks'].append(1)
    else:
        p1['ICOmarks'].append(0)
    if str(base['Raised_money(ICOdrops)'][i])!='nan' or str(base['Enddate(ICOdrops)'][i])!='nan'\
            or str(base['Website(ICOdrops)'][i])!='nan' or str(base['Startdate(ICOdrops)'][i])!='nan':
        p1['ICOdrops'].append(1)
    else:
        p1['ICOdrops'].append(0)
    if str(base['Symbol(cryptocompare)'][i])!='nan' or str(base['Raised(cryptocompare)'][i])!='nan' or str(base['Startdate(cryptocompare)'][i])!='nan'\
            or str(base['StartPriceCurrency(cryptocompare)'][i])!='nan' or str(base['TokenSupply(cryptocompare)'][i])!='nan':
        p1['Cryptocompare'].append(1)
    else:
        p1['Cryptocompare'].append(0)

ddd = pd.DataFrame(p1)
ddd = ddd[['Name', 'Start_date', 'End_date', 'Start_date_tokenmarket', 'End_date_tokenmarket', 'Start_date_ICOmarks', 'End_date_ICOmarks', 'Start_date_cryptocompare', 'End_date_cryptocompare', 'Start_date_ICOdrops', 'End_date_ICOdrops', 'Raised_money (USD)', 'Raised_money_ICOmarks (USD)', 'Raised_money_cryptocompare (USD)', 'Raised_money_ICOdrops (USD)', 'Github', 'Facebook', 'Linkedin', 'Telegram', 'Twitter', 'Reddit', 'Medium', 'Failure', 'Tokendata', 'Tokenmarket', 'Coinmarketcap', 'ICOmarks', 'ICOdrops', 'Cryptocompare']]

ddd.to_csv('/users/barry/desktop/p1.csv')