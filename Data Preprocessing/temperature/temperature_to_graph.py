"""
Extract the values from room_temperature.csv.gz for each roomid 
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
filtered_file_paths = glob.glob(path_to_household_sensors + "/*room_temperature.csv.gz")
path_to_figures = r'C:\Users\User\Desktop\household_sensors\temperature_graphs'

home_ids = []    #list of all home ids
home_ids_int = []   #list of all home ids converted to int
home_ids_rooms = []   #list of all rooms per homeid
home_ids_rooms_no_underscore = []
df = pd.DataFrame()    #room_temperature csv
i=0

if not os.path.exists(path_to_figures): 
    if not os.path.exists(path_to_figures):
        os.mkdir(path_to_figures)

for d_path in filtered_file_paths:    #insert homeid in home_ids
    home_ids.append(re.findall('(?<=home).[0-9]+', d_path))

for d_path in filtered_file_paths:    #insert homeid and roomid home_ids_rooms
    home_ids_rooms.append(re.findall('(?<=home)[^_]*_[^_]*', d_path))
       
for string_list in home_ids:    #convert of home_ids to int
    for string in string_list:
        home_ids_int.append(int(string))  
        
for string_list in home_ids_rooms:    #replace of underscore in "home_ids_rooms_no_underscore" with space
    for string in string_list:
        string_no_underscore = string.replace("_", "")
        string_no_underscore = re.sub("[A-Za-z]+", lambda group: " " + group[0] + " ", string_no_underscore)
        home_ids_rooms_no_underscore.append(string_no_underscore)          
        
for d_path in filtered_file_paths:    #φόρτωση των csv στο df   
    df = pd.read_csv(d_path, compression='gzip', sep=',', quotechar='"', 
                                            on_bad_lines='skip',
                                            names=["Date", "Temperature"])
    df = df[df.Temperature != 0]
    df['Temperature'] = df['Temperature'].apply(lambda x: x/10)    #temperature value in the dataset is multiplied x10
    df.index = pd.to_datetime(df['Date'])
    df.drop('Date', axis = 1, inplace = True)
    for j in df:
        X = df.index
        Y = df.values
        fig, ax = plt.subplots()
        ax.plot_date(X, Y, markerfacecolor='black', markeredgecolor='blue', markeredgewidth=0.1 , ms=2)
        fig.autofmt_xdate()
        ax.xaxis.set_major_locator(ticker.MultipleLocator(30))
        ax.tick_params(axis='both', which='major', labelsize=6)
        ax.set_xlim([datetime.date(2016, 7, 1), datetime.date(2018, 9, 1)])
        ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
        ax.set_ylim([-10, 50])
    plt.title('Home ' + home_ids_rooms_no_underscore[i], fontsize=9)
    plt.legend(['Temperature (°C)'], loc = 'upper left', fontsize=6)
    ftitle = 'Home_' + str(home_ids_rooms[i][0])
    fname = '%s.png' % ftitle
    plt.savefig(os.path.join(path_to_figures, fname), bbox_inches = 'tight', dpi=300)
    i += 1