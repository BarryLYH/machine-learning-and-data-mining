import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pylab as plt


def redata(data):
    mean = np.mean(data)
    std = np.std(data)
    return [((i-mean)/std) for i in data]

data = pd.read_csv('/users/barry/desktop/DATA_BTC.csv')
date = data['DATE']
date = pd.to_datetime(date)
data['DATA'] = date

btc_usd = redata(data['BTC/USD'])
t_volume = redata(data['BTC_TRANS_VLOUME'])
m_diff = redata(data['mining_diff'])
hash = redata(data['hash_rate'])
effr = redata(data['EFFR'])
usd_num = redata(data['USD_supply'])
trend = redata(data['google_trend'])
gold = redata(data['GOLD'])
lite = redata(data['litecoin'])
database = []
for i in range(len(btc_usd)):
    database.append([float(btc_usd[i]), float(t_volume[i]), float(m_diff[i]), float(hash[i]), float(effr[i]),
                    float(usd_num[i]), float(trend[i]), float(gold[i]), float(lite[i])])

plt.plot(btc_usd)
plt.show()