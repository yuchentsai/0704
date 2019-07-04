import time
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web
import sys


style.use('ggplot')
start = dt.datetime(2018,1,1)
end = dt.datetime(2019,6,27)
df = web.DataReader('2330.TW','yahoo',start,end)
time.sleep(1)
print(df.tail())
df = web.DataReader('2331.TW','yahoo',start,end)
time.sleep(1)
print(df.tail())
df = web.DataReader('2332.TW','yahoo',start,end)
time.sleep(1)
print(df.tail())