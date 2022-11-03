#plot_bar_series.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
import csv

data = pd.read_csv("c:\\python\\test\\timeseries.csv", usecols=['Date','B1.IPR', 'B11.IPR'],parse_dates=['Date'],
                                             index_col=['Date'] )

#Bar chart
fig, ax = plt.subplots(figsize=(10, 7))
data.plot(kind='bar', ax=ax)
plt.ylim(90, 120)
X = plt.gca().xaxis
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=2))
#format date
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

plt.show()
