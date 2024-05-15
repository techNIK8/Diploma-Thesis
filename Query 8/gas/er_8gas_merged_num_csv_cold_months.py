"""
@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\merged_numeric_cold_months.csv')

df['high_floor_area_per_room'] = df['floorarea_per_room_mean'].apply(lambda x: 1 if x > df['floorarea_per_room_mean'].mean() else 0)

df['high_gas_pulse_consumption'] = df['gas_pulse_per_cold_months_mean'].apply(lambda x: 1 if x > df['gas_pulse_per_cold_months_mean'].mean() else 0)

df.drop('homeid', axis=1, inplace=True)
df.drop('number_of_rooms', axis=1, inplace=True)
df.drop('floorarea_per_room_mean', axis=1, inplace=True)
df.drop('temperature_per_cold_months_mean', axis=1, inplace=True)
df.drop('gas_pulse_per_cold_months_mean', axis=1, inplace=True)

df.to_csv(r'C:\Users\User\Desktop\household_sensors\er_8gas.csv', index=False)

