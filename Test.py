import datetime as dt
from datetime import date
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2019,12,31)
today = date.today()

df = web.DataReader('XAW.TO', 'yahoo', today, today)

#print(df.head())
#print(df.tail())
df.to_csv('XAW.csv')

df = pd.read_csv('XAW.csv', parse_dates=True, index_col=0)
df['Close'].plot()
df['Adj Close'].plot()
plt.show()