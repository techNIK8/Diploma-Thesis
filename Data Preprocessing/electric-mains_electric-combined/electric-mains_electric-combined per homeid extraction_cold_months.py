"""
Extract the electric consumption values from electric-mains_electric-combined.csv.gz 
for each homeid, save only the values for cold months,
find the average and save it in a new csv file with the 
corresponding homeid.

@author: Nikos Kosioris
"""

import glob 
import pandas as pd
import re

path_to_household_sensors = r'C:\Users\User\Desktop\IDEAL_Household_Energy_Dataset\household_sensors'
filtered_file_paths = glob.glob(path_to_household_sensors + '/*electric-mains_electric-combined.csv.gz')
path_to_csv = r'C:\Users\User\Desktop\household_sensors\final_mean_electric-mains_electric-combined_cold_months.csv'

home_ids = []    #list of all home ids
home_ids_int = []   #list of all home ids converted to int
df = pd.DataFrame()    #electric_mains_electric_combined csv
df_2 = pd.DataFrame(columns=['homeid', 'electric_con_per_cold_months_mean'])    #mean of electric_mains_electric_combined for cold months per homeid
i = 0

for d_path in filtered_file_paths:    #insert homeid in home_ids
    home_ids.append(re.findall('(?<=home).[0-9]+', d_path))
        
for string_list in home_ids:    #convert of home_ids to int
    for string in string_list:
        home_ids_int.append(int(string))  

for d_path in filtered_file_paths:    #load csv in df   
    df = pd.read_csv(d_path, compression='gzip', sep=',', quotechar='"', 
                                           on_bad_lines='skip',
                                           names=['Date', 'electric_mains_electric_combined'])
    df = df.iloc[1:]    #delete first row because it has value = 0
    df.index = pd.to_datetime(df['Date'])
    df.drop('Date', axis = 1, inplace = True)
    mask = (df.index >= '2017-9-1') & (df.index < '2018-3-1')
    df_mask = df.loc[mask]  
    df_temp = pd.DataFrame([df_mask['electric_mains_electric_combined'].mean()], columns=['electric_con_per_cold_months_mean'])
    df_2 = pd.concat([df_2,df_temp], ignore_index=True)
    df_2.at[i, 'homeid'] = home_ids_int[i]     #insert of homeid in df_2    
    i += 1

df_2['homeid'] = df_2['homeid'].astype('int')    #delete decimal part of homeid in df_2
df_2['electric_con_per_cold_months_mean'] = df_2['electric_con_per_cold_months_mean'].round(decimals = 2)     #μείωση ακρίβειας σε δυο δεκαδικά ψηφία
df_2.to_csv(path_to_csv, index=False)