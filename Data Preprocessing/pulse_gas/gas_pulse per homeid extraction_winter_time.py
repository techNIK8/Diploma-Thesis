"""
Extract the gas values from pulse_gas.csv.gz for each homeid, 
save only the values for winter time, calculate the average and 
save it in a new csv file with the corresponding homeid. 
    
@author: Nikos Kosioris
"""

import glob 
import pandas as pd
import re

path_to_household_sensors = r'C:\Users\User\Desktop\IDEAL_Household_Energy_Dataset\household_sensors'
filtered_file_paths = glob.glob(path_to_household_sensors + '/*pulse_gas.csv.gz')
path_to_csv = r'C:\Users\User\Desktop\household_sensors\final_mean_pulse_gas_winter_time.csv'

home_ids = []    #list of all home ids
home_ids_int = []   #list of all home ids converted to int
df = pd.DataFrame()    #pulse_gas csv
df_2 = pd.DataFrame(columns=['homeid', 'gas_pulse_per_winter_time_mean'])    #mean of gas pulse values for winter time per homeid
i = 0

for d_path in filtered_file_paths:    #insert homeid in home_ids
    home_ids.append(re.findall('(?<=home).[0-9]+', d_path))
        
for string_list in home_ids:    #convert of home_ids to int
    for string in string_list:
        home_ids_int.append(int(string))  

for d_path in filtered_file_paths:    #load csv in df   
    df = pd.read_csv(d_path, compression='gzip', sep=',', quotechar='"', 
                                           on_bad_lines='skip',
                                           names=['Date', 'gas_pulse'])
    df.index = pd.to_datetime(df['Date'])
    df.drop('Date', axis = 1, inplace = True)
    mask = (df.index >= '2017-10-29') & (df.index < '2018-3-25')
    df_mask = df.loc[mask]
    df_temp = pd.DataFrame([df_mask['gas_pulse'].mean()], columns=['gas_pulse_per_winter_time_mean'])
    df_2 = pd.concat([df_2,df_temp], ignore_index=True)
    df_2.at[i, 'homeid'] = home_ids_int[i]     #insert of corresponding homeid in df_2
    i += 1

df_2['homeid'] = df_2['homeid'].astype('int')    #delete decimal part of homeid in df_2
df_2['gas_pulse_per_winter_time_mean'] = df_2['gas_pulse_per_winter_time_mean'].round(decimals = 2)     #round value to two decimals
df_2.to_csv(path_to_csv, index=False)