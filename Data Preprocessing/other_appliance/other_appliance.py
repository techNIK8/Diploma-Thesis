"""
Create a column for each type of electrical device and save the number of devices for each homeid

@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\other_appliance.csv')

df['number'] = df['number'].str.replace('+',' ')
df_2 = df.pivot_table('number', ['homeid'], 'appliance_name')
df_2 = df_2.fillna(0)
df_2 = df_2.astype('int') 
df_2 = df_2.drop('outdoor_gas_space_heater', axis=1)

df_2.to_csv(r'C:\Users\User\Desktop\household_sensors\final_other_appliance.csv')