# plot_time_series.py

import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from matplotlib import dates as mpl_dates
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
    
plt.style.use('seaborn')
fig, ax = plt.subplots(figsize=(10, 7))
data = pd.read_csv("c:\\python\\test\\kpi.csv", usecols=['Date','B1.IPR'],parse_dates=['Date'],
                                             index_col=['Date'] )
ax.plot(data)
X = plt.gca().xaxis

#set ticks every month
ax.xaxis.set_major_locator(mpl_dates.MonthLocator(interval=2))
#format date
ax.xaxis.set_major_formatter(mpl_dates.DateFormatter('%Y-%m-%d'))
plt.gcf().autofmt_xdate()
date_format = mpl_dates.DateFormatter('%Y-%m-%d')
plt.gca().xaxis.set_major_formatter(date_format)
plt.tight_layout()
plt.title('Series Data')
plt.xlabel('Date')
plt.ylabel('Values')
plt.show()