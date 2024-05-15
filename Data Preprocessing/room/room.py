"""
1)Sum external windows, external doors and external walls per homeid and store the values in new columns
2)Calculate cubic centimetres of each house
3)Sum radiators by homeid
4)Replace "unknown" value of the clothesdrying column with "never"
5)For each room that has the value "sometimes" or "often" in clothesdrying column, calculate the cubic meters of the room and calculate the percentage in relation to the total cubic meters of the house
6)Per homeid, for each room that has radiator = 1 and trvs = "some" or "all", sum up the total cubic metres and calculate the % in relation to the total cubic metres of the house
7)Sum the number of rooms in each house

@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\room.csv')

df_2 = pd.DataFrame()

df_2 = df.groupby(['homeid'])['externalwindows', 'externaldoors', 'externalwalls'].sum()
df_2 = df.groupby(['homeid'])['floorarea', 'height'].mean()
df_2.rename(columns = {'floorarea':'floorarea_per_room_mean', 'height':'height_per_room_mean'}, inplace = True)
df_2['floorarea_per_room_mean'] = df_2['floorarea_per_room_mean'].round(decimals = 2)     #round value to two decimals
df_2['height_per_room_mean'] = df_2['height_per_room_mean'].round(decimals = 2)     #round value to two decimals
df['cubic_area'] = df['floorarea'] * df['height']
cubic_area_list = df.groupby(['homeid'])['cubic_area'].sum()
df_2['cubic_area'] = cubic_area_list
radiators_sum = df.groupby(['homeid'])['radiators'].sum()
df_2['radiators'] = radiators_sum
windowsopen_sum = df.groupby(['homeid'])['windowsopen'].sum()
df_2['windowsopen'] = windowsopen_sum
externaldoors_sum = df.groupby(['homeid'])['externaldoors'].sum()
df_2['externaldoors'] = externaldoors_sum
externalwalls_sum = df.groupby(['homeid'])['externalwalls'].sum()
df_2['externalwalls'] = externalwalls_sum
externalwindows_sum = df.groupby(['homeid'])['externalwindows'].sum()
df_2['externalwindows'] = externalwindows_sum
df['clothesdrying'] = df['clothesdrying'].str.replace('unknown','never')
df_2['number_of_rooms'] = df.groupby('homeid').size()

df.loc[(df['clothesdrying'] == 'sometimes') | (df['clothesdrying'] == 'often'), 'cubic_area_for_clothesdrying'] = df['cubic_area']
df['cubic_area_for_clothesdrying'] = df['cubic_area_for_clothesdrying'].fillna(0)
cubic_area_for_clothesdrying_list = df.groupby(['homeid'])['cubic_area_for_clothesdrying'].sum()
df_2['cubic_area_for_clothesdrying_percent'] = cubic_area_for_clothesdrying_list / df_2['cubic_area'] * 100
df_2['cubic_area_for_clothesdrying_percent'] = df_2['cubic_area_for_clothesdrying_percent'].round(decimals = 2)     #round value to two decimals

df.loc[(df['radiators'] == 1) & (df['trvs'] == 'All'), 'cubic_area_with_trvs' ] = df['cubic_area']
df['cubic_area_with_trvs'] = df['cubic_area_with_trvs'].fillna(0)
cubic_area_with_trvs_list = df.groupby(['homeid'])['cubic_area_with_trvs'].sum()
df_2['cubic_area_with_trvs_percent'] = cubic_area_with_trvs_list / df_2['cubic_area'] * 100
df_2['cubic_area_with_trvs_percent'] = df_2['cubic_area_with_trvs_percent'].round(decimals = 2)     #round value to two decimals

df_2.to_csv(r'C:\Users\User\Desktop\household_sensors\final_room.csv')