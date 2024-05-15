"""
Extract the values from gas-pulse_gas.csv.gz for each homeid 
(hourly readings from the auxiliarydata folder were used because of low computational 
power), convert the values of each "Date" column to datetime type and save the graph 
in a png file with the corresponding homeid

@author: Nikos Kosioris
"""

import glob 
import pandas as pd
import re
import os
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import matplotlib.ticker as ticker

path_to_household_sensors = r'C:\Users\User\Desktop\IDEAL_Household_Energy_Dataset\auxiliarydata\hourly_readings'
filtered_file_paths = glob.glob(path_to_household_sensors + '/*gas-pulse_gas.csv.gz')
path_to_figures = r'C:\Users\User\Desktop\household_sensors\pulse_gas_graphs'

home_ids = []    #list of all home ids
home_ids_int = []   #list of all home ids converted to int
df = pd.DataFrame()    #room_humidity csv
i=0

if not os.path.exists(path_to_figures): 
    if not os.path.exists(path_to_figures):
        os.mkdir(path_to_figures)

for d_path in filtered_file_paths:    #insert homeid in home_ids
    home_ids.append(re.findall('(?<=home).[0-9]+', d_path))
       
for string_list in home_ids:    #convert of home_ids to int
    for string in string_list:
        home_ids_int.append(int(string))  

for d_path in filtered_file_paths:    #load csv in df   
    df = pd.read_csv(d_path, compression='gzip', sep=',', quotechar='"', 
                                            on_bad_lines='skip',
                                            names=["Date", "Gas Pulse"])    
    df = df.iloc[1:]    #delete the first row because it has a value of 0
    df.index = pd.to_datetime(df['Date'])
    df.drop('Date', axis = 1, inplace = True)
    for j in df:
        X = df.index
        Y = df.values
        fig, ax = plt.subplots()
        ax.plot_date(X, Y, markerfacecolor='black', markeredgecolor='green', markeredgewidth=0.1 , ms=2)
        fig.autofmt_xdate()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
        ax.tick_params(axis='both', which='major', labelsize=6)
        ax.set_xlim([datetime.date(2016, 7, 1), datetime.date(2018, 9, 1)])
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
        ax.set_ylim([0, 1000000])
    plt.title('Home ' + str(home_ids_int[i]), fontsize=9)
    plt.legend(['Gas Pulse (Wh)'], loc = 'upper left', fontsize=6)
    ftitle = 'Home_' + str(home_ids_int[i])
    fname = '%s.png' % ftitle
    plt.savefig(os.path.join(path_to_figures, fname), bbox_inches = 'tight', dpi=300)
    i += 1