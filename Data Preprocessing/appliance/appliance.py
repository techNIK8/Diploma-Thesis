"""
Create a column for each type of electrical device available and save the number of devices for each homeid

@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\appliance.csv')

df['appliancetype'] = df['appliancetype'] + '_' + df['powertype']
df.drop(df.loc[df['homeid'] == 55].index, inplace=True)   #drop homeid = 55 because there is not enough data in other csv files
df_2 = df.pivot_table('number', ['homeid'], 'appliancetype')
df_2 = df_2.fillna(0)
df_2 = df_2.astype('int') 

df_2.to_csv(r'C:\Users\User\Desktop\household_sensors\final_appliance.csv')