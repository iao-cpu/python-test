import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from pandas.plotting import register_matplotlib_converters
import csv

#fig, ax = plt.subplots()
#fig= plt.figure(figsize=(10,5))
#fig.autofmt_xdate()
#ax.fmt_xdata = mdates.DateFormatter('%Y-%m-%d')

#df = pd.read_csv("c:\\python\\test\\kpi.csv", parse_dates=['Date'],index_col=['Date'],dayfirst=True)

# Import file into pandas dataframe, identifying the date column to be converted to datetime

#set ggplot style
#plt.style.use('ggplot')
a=[]
dates=[]
x=0

df = pd.read_csv("c:\\python\\test\\timeseries.csv", usecols=['Date','B1.IPR','B11.IPR'],parse_dates=['Date'],
                                              index_col=['Date'])


with open("c:\\python\\test\\timeseries.csv") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:  
        print(row)
        a.append(row) 

# View data index
print(df.index)
print(df.head())
print(df.dtypes)
#print(a.index("Jan-01-2016"))


# Query the data type for date column
#type(df['Date'][0])

# Create the plot space upon which to plot the data
fig, ax = plt.subplots(figsize=(10, 7))

# Add the x-axis and the y-axis to the plot
ax.plot(df)
plt.gcf().autofmt_xdate

#Bar chart
fig, ax = plt.subplots(figsize=(10, 7))
#ax.bar(df.index, df['B1.IPR'])
plt.ylim(90, 120)
plt.xlim(90, 120)
df.plot(kind='bar', ax=ax)


#ax.bar(df, y_pos, align = 'center', color='purple')

# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Values",
       title="Series Data")

# Clean up the x axis dates (reviewed in lesson 4)
ax.xaxis.set_major_locator(mdates.WeekdayLocator(interval=10))
ax.xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))



""" plt.pie(df,
labels=' ',
startangle=90,
shadow=True,
explode=(0.1,0.1,0,0),
autopct='%1.1f%%') """

#df.plot()
""" plt.plot(df)
plt.title("Series Data")
plt.xlabel("Date")
plt.ylabel("B1.IPR") """

plt.show()