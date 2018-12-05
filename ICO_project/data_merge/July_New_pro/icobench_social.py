import pandas as pd

d = {'Name':[], 'Facebook':[], 'Github':[], 'Reddit':[], 'Bitcointalk':[], 'Blog':[],
              'Medium':[], 'Twitter':[], 'Slack':[], 'Telegram':[], 'Website':[], 'Discord':[], 'VK':[]}

b = pd.read_csv('/users/barry/desktop/icobench_2.csv', encoding = "ISO-8859-1")

base = b.to_dict(orient="list")

soc = base['Social_links']
name = base['Name']

for i in range(len(name)):
    print(i)
    dd = {'Name':'NA', 'Facebook':'NA', 'Github':'NA', 'Reddit':'NA', 'Bitcointalk':'NA', 'Blog':'NA',
          'Medium':'NA', 'Twitter':'NA', 'Slack':'NA', 'Telegram':'NA', 'Website':'NA', 'Discord':'NA',
          'VK':'NA'}
    dd['Name'] = name[i]
    if str(soc[i]) != 'nan':
        print(name[i], soc[i])
        social = soc[i].split('\\n')
        for link in social:
            if 'facebook' in link:
                dd['Facebook'] = link
            elif 'github' in link:
                dd['Github'] = link
            elif 'reddit' in link:
                dd['Reddit'] = link
            elif 'bitcointalk' in link:
                dd['Bitcointalk'] = link
            elif 'medium' in link:
                dd['Medium'] = link
            elif 'twitter' in link:
                dd['Twitter'] = link
            elif 'slack' in link:
                dd['Slack'] = link
            elif 't.me' in link or 'telegram.me' in link:
                dd['Telegram'] = link
            elif 'source=icobench' in link:
                dd['Website'] = link
            elif 'discord' in link:
                dd['Discord'] = link
            elif 'blog.' in link:
                dd['Blog'] = link
            elif 'vk.com' in link:
                dd['VK'] = link
            else:
                print(link)
    for index in dd:
        if dd[index] == 'NA':
            d[index].append(' ')
        else:
            d[index].append(dd[index])

ddd = pd.DataFrame(d)
ddd.to_csv('/users/barry/desktop/basss.csv')