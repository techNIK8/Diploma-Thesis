"""
Extract the light values from room_light.csv.gz for each roomid, 
save only the values for winter time, calculate the average for each homeid and 
save it in a new csv file with the corresponding homeid. 
    
@author: Nikos Kosioris
"""

import glob 
import pandas as pd
import re

path_to_household_sensors = r'C:\Users\User\Desktop\IDEAL_Household_Energy_Dataset\auxiliarydata\light'
filtered_file_paths = glob.glob(path_to_household_sensors + '/*room_light.csv.gz')
path_to_csv = r'C:\Users\User\Desktop\household_sensors\final_mean_light_per_room_winter_time.csv'
path_to_csv_2 = r'C:\Users\User\Desktop\household_sensors\final_mean_light_winter_time.csv'

home_ids = []    #list of all home ids
home_ids_int = []   #list of all home ids converted to int
home_ids_rooms = []   #list of all rooms per homeid
df = pd.DataFrame()    #room_light csv
df_2 = pd.DataFrame(columns=['homeid', 'room', 'light_per_winter_time_mean'])    #mean of light values for winter time per homeid
df_3 = pd.DataFrame
i = 0

for d_path in filtered_file_paths:    #insert homeid in home_ids
    home_ids.append(re.findall('(?<=home).[0-9]+', d_path))
    
for d_path in filtered_file_paths:    #insert homeid and roomid home_ids_rooms
    home_ids_rooms.append(re.findall('(?<=home)[^_]*_[^_]*', d_path))    
        
for string_list in home_ids:    #convert of home_ids to int
    for string in string_list:
        home_ids_int.append(int(string))  

for d_path in filtered_file_paths:    #load csv in df  
    df = pd.read_csv(d_path, compression='gzip', sep=',', quotechar='"', 
                                            on_bad_lines='skip',
                                            names=['Date', 'Light'])
    df.index = pd.to_datetime(df['Date'])
    df.drop('Date', axis = 1, inplace = True)
    mask = (df.index >= '2017-10-29') & (df.index < '2018-3-25')  
    df_mask = df.loc[mask]
    df_temp = pd.DataFrame([df_mask['Light'].mean()], columns=['light_per_winter_time_mean'])  
    df_2 = pd.concat([df_2,df_temp], ignore_index=True)
    df_2.at[i, 'homeid'] = home_ids_int[i]     #insert of corresponding homeid in df_2
    df_2.at[i, 'room'] = home_ids_rooms[i][0]     #insert of corresponding roomid in df_2 
    i += 1

df_3 = df_2.groupby(['homeid'])['light_per_winter_time_mean'].mean().reset_index()
df_3['homeid'] = df_3['homeid'].astype('int')    #delete decimal part of homeid in df_3
df_3['light_per_winter_time_mean'] = df_3['light_per_winter_time_mean'].round(decimals = 2)     #round value to two decimals
df_3.to_csv(path_to_csv_2, index=False)

df_2['homeid'] = df_2['homeid'].astype('int')    #delete decimal part of homeid in df_2
df_2['light_per_winter_time_mean'] = df_2['light_per_winter_time_mean'].round(decimals = 2)     #round value to two decimals
df_2.to_csv(path_to_csv, index=False)