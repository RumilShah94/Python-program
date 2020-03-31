#Rumil Shah
#Simple Moving CrossOver Strategy using Python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import quandl
from matplotlib import style
style.use('fivethirtyeight')

#Make a file 'auth.txt' 
api_key=open('auth.txt','r').read()

#Data is choosen from 01/08/2018 to 11/02/2019 for Equity of Punjab National Bank(Data is obtained from Quandl)
data=quandl.get('NSE/PNB', trim_start ='2018-08-01', trim_end='2019-02-11',api_key=api_key)

#Calculating SMA for 15 & 40 days
data['15days']= np.round(data['Close'].rolling(window=15).mean(),2)
data['40days']= np.round(data['Close'].rolling(window=40).mean(),2)

#Optional (only if you want data in tabular form)
print(data)

#Plotting Closing prices vs SMA
data[['Close','15days','40days']].plot(grid=True,figsize=(10,15))

plt.show()


                                   
