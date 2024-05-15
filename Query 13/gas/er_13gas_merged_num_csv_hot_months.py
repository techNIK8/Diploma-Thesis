"""
@author: Nikos Kosioris
"""


import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\merged_numeric_hot_months.csv')

df.loc[(df['urban_rural_name_Large_Urban_Areas'] == 1) | 
           (df['urban_rural_name_Other_Urban_Areas'] == 1)
           , 'urban_area'] = 1

df['urban_area'] = df['urban_area'].fillna(0)
df['urban_area'] = df['urban_area'].astype('int')

df['high_gas_pulse_consumption'] = df['gas_pulse_per_hot_months_mean'].apply(lambda x: 1 if x > df['gas_pulse_per_hot_months_mean'].mean() else 0)

df.drop('homeid', axis=1, inplace=True)
df.drop('urban_rural_name_Large_Urban_Areas', axis=1, inplace=True)
df.drop('urban_rural_name_Other_Urban_Areas', axis=1, inplace=True)
df.drop('urban_rural_name_Small_Towns_or_Rural_Areas', axis=1, inplace=True)
df.drop('gas_pulse_per_hot_months_mean', axis=1, inplace=True)
df.drop('temperature_per_hot_months_mean', axis=1, inplace=True)
df.drop('number_of_rooms', axis=1, inplace=True)

df.to_csv(r'C:\Users\User\Desktop\household_sensors\er_13gas.csv', index=False)

