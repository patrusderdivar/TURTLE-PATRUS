from backtesting import Backtest, Strategy
import pandas_ta as ta
import pandas as pd
import numpy as np
from datetime import time, timedelta, datetime
import ccxt
import numpy as np
import warnings
from backtesting.lib import crossover
import math

#warnings.filterwarnings('ignore')



exchange = ccxt.binanceus()

from_ts = exchange.parse8601('2023-02-01 00:00:00')

ohlcv = exchange.fetch_ohlcv('BTC/USDT', timeframe='4h', since = from_ts,  limit = 1000) #daily candles with 200 day.(200 candle)

ohlcv_list=[]

ohlcv_list.append(ohlcv)
while True:
    from_ts = ohlcv[-1][0]
    new_ohlcv = exchange.fetch_ohlcv('BTC/USDT', '4h', since=from_ts, limit=1000)
    ohlcv.extend(new_ohlcv)
    if len(new_ohlcv)!=1000:
        break

df= pd.DataFrame(ohlcv[:-1], columns= ['timestamp','Open', 'High', 'Low', 'Close', 'Volume'])
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

data = df

data = data.set_index('timestamp')

print("data checked.")
print(df.head())