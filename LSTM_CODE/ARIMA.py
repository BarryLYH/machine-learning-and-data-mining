import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import sys
from statsmodels.tsa.arima_model import ARMA, ARIMA
import statsmodels.api as sm
import warnings
from statsmodels.tsa.stattools import adfuller
import arrow

#差分
def diff_ts(ts, d):
    global shift_ts_list
    global last_data_shift_list
    shift_ts_list = []
    last_data_shift_list = []
    tmp_ts = ts
    for i in d:
        last_data_shift_list.append(tmp_ts[-i])
        shift_ts = tmp_ts.shift(i)
        shift_ts_list.append(shift_ts)
        tmp_ts = tmp_ts - shift_ts
    tmp_ts.dropna(inplace=True)
    return tmp_ts
# 还原操作
def predict_diff_recover(predict_value, d):
    if isinstance(predict_value, float):
        tmp_data = predict_value
        for i in range(len(d)):
            tmp_data = tmp_data + last_data_shift_list[-i-1]
    elif isinstance(predict_value, np.ndarray):
        tmp_data = predict_value[0]
        for i in range(len(d)):
            tmp_data = tmp_data + last_data_shift_list[-i-1]
    else:
        tmp_data = predict_value
        for i in range(len(d)):
            try:
                tmp_data = tmp_data.add(shift_ts_list[-i-1])
            except:
                raise ValueError('What you input is not pd.Series type!')
        tmp_data.dropna(inplace=True)
    return tmp_data
#ADF 检测
def adf_test(timeseries):
    rolling_statistics(timeseries)#绘图
    print('Results of Augment Dickey-Fuller Test:')
    dftest = adfuller(timeseries, autolag='AIC')
    dfoutput = pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])
    for key,value in dftest[4].items():
        dfoutput['Critical Value (%s)'%key] = value
    print(dfoutput)
#滚动统计
def rolling_statistics(timeseries):
    #Determing rolling statistics
    rolmean = timeseries.rolling(center=False,window=12).mean()
    rolstd = timeseries.rolling(window=12,center=False).std()
    #Plot rolling statistics:
    orig = plt.plot(timeseries, color='blue',label='Original')
    mean = plt.plot(rolmean, color='red', label='Rolling Mean')
    std = plt.plot(rolstd, color='black', label = 'Rolling Std')
    plt.legend(loc='best')
    plt.title('Rolling Mean & Standard Deviation')
    plt.show()
#AIC 筛选p,q
def aic(ts_log_diff, maxLag):
    best_p = 0
    best_q = 0
    best_aic = sys.maxsize
    best_model=None
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore")
        for p in np.arange(maxLag):
            for q in np.arange(maxLag):
                model = ARMA(ts_log_diff, order=(p, q))
                try:
                    results_ARMA = model.fit(disp=-1)
                except:
                    continue
                aic = results_ARMA.aic
                if aic < best_aic:
                    best_p = p
                    best_q = q
                    best_aic = aic
                    best_model = results_ARMA
    print(best_p,best_q,best_model)
#BIC 筛选p,q
def bic(ts_log_diff, maxLag):
    best_p = 0
    best_q = 0
    best_bic = sys.maxsize
    best_model=None
    with warnings.catch_warnings():
        warnings.filterwarnings("ignore")
        for p in np.arange(maxLag):
            for q in np.arange(maxLag):
                model = ARMA(ts_log_diff, order=(p, q))
                try:
                    results_ARMA = model.fit(disp=-1)
                except:
                    continue
                bic = results_ARMA.bic
                #print(bic, best_bic)
                if bic < best_bic:
                    best_p = p
                    best_q = q
                    best_bic = bic
                    best_model = results_ARMA
    print(best_p,best_q,best_model)
#acf和pacf画图
def acf_pacf_plot(ts_log_diff):
    sm.graphics.tsa.plot_acf(ts_log_diff,lags=40) #ARIMA,q
    sm.graphics.tsa.plot_pacf(ts_log_diff,lags=40) #ARIMA,p
    plt.show()
#ARIMA 模型建模
def arima_model(ts_log, p, d, q):
    global ts_log_diff
    model = ARIMA(ts_log, order=(p, d, q))
    results_ARIMA = model.fit(disp=-1)
    plt.plot(ts_log_diff)
    #plt.plot(results_ARIMA.fittedvalues, color='red')  # 和下面这句结果一样
    plt.plot(results_ARIMA.predict(), color='black')  # predict得到的就是fittedvalues，只是差分的结果而已。还需要继续回退
    plt.title('RSS: %.4f' % sum((results_ARIMA.fittedvalues - ts_log_diff) ** 2))
    plt.show()
#ARIMA 数据还原
def recover_data(ts_log, p, d, q):
    global ts_log_diff
    model = ARIMA(ts_log, order=(p, d, q))
    results_ARIMA = model.fit(disp=-1)
    predict_ts = results_ARIMA.predict()

    diff_recover_ts = predict_diff_recover(predict_ts, d=[1])  # 恢复差分数据
    log_recover = np.exp(diff_recover_ts)  # 还原对数数据

    # ts = ts[log_recover.index]#排除空的数据
    plt.plot(ts, color="blue", label='Original')
    plt.plot(log_recover, color='red', label='Predicted')
    plt.legend(loc='best')
    plt.title('RMSE: %.4f' % np.sqrt(sum((log_recover - ts) ** 2) / len(ts)))  # RMSE,残差平方和开根号，即标准差
    plt.show()
#ARIMA 预测走势
def arima_predict(ts_log, p, d, q):
    global ts_log_diff, forecast_n
    model = ARIMA(ts_log, order=(p, d, q))
    results_ARIMA = model.fit(disp=-1)
    forecast_arima_log = results_ARIMA.forecast(forecast_n)
    forecast_arima_log = forecast_arima_log[0]
    print(forecast_arima_log)

    new_index = get_date_range('1986-08-22', forecast_n)
    forecast_arima_log = pd.Series(forecast_arima_log, copy=True, index=new_index)
    print(forecast_arima_log.head())

    forecast_arima = np.exp(forecast_arima_log)
    plt.plot(ts, label='Original', color='blue')
    plt.plot(forecast_arima, label='Forcast', color='red')
    plt.legend(loc='best')
    plt.title('forecast')
    plt.show()
    return forecast_arima
#定义预测起始天数start， 和预测天数limit
def get_date_range(start, limit, level='day',format='YYYY-MM-DD'):
    start = arrow.get(start, format)
    result=(list(map(lambda dt: dt.format(format) , arrow.Arrow.range(level, start, 		   limit=limit))))
    dateparse2 = lambda dates:pd.datetime.strptime(dates,'%Y-%m-%d')
    return map(dateparse2, result)



#######################################################################################
#主程序
if __name__=='__main__':
    forecast_n = 30

    data = pd.read_csv('/users/barry/desktop/DATA.csv')
    date = data['Date']
    date = pd.to_datetime(date)
    data["Date"] = date
    ts = pd.Series(data['Open'].values, index=data['Date'])



    ts_log = np.log(ts)
    ts_log.dropna(inplace=True)
    ts_log_diff = diff_ts(ts_log, [1])
    ts_log_diff.dropna(inplace=True)
    #plt.show(plt.plot(ts))
    #plt.show(plt.plot(ts_log))
    #plt.show(plt.plot(ts_log_diff))


    #adf_test(ts_log_diff)

    #rolling_statistics(ts_log_diff)

    #acf_pacf_plot(ts_log_diff)

    #aic(ts_log_diff, 10)

    #bic(ts_log_diff, 10)

    #arima_model(ts_log, 5, 1, 5)

    #recover_data(ts_log, 5, 1, 5)

    arima_predict(ts_log, 5, 1, 5)

