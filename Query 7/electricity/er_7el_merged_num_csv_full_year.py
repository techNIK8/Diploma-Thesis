"""
@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\merged_numeric_full_year.csv')

df['cubic_area_per_room_mean'] = df['cubic_area'] / df['number_of_rooms']
df['cubic_area_per_room_mean'] = df['cubic_area_per_room_mean'].round(decimals = 2)     #μείωση ακρίβειας σε δυο δεκαδικά ψηφία

df['high_cubic_area_per_room'] = df['cubic_area_per_room_mean'].apply(lambda x: 1 if x > df['cubic_area_per_room_mean'].mean() else 0)

df['high_electric_consumption'] = df['electric_con_per_full_year_mean'].apply(lambda x: 1 if x > df['electric_con_per_full_year_mean'].mean() else 0)

df.drop('homeid', axis=1, inplace=True)
df.drop('electric_con_per_full_year_mean', axis=1, inplace=True)
df.drop('cubic_area', axis=1, inplace=True)
df.drop('temperature_per_full_year_mean', axis=1, inplace=True)
df.drop('number_of_rooms', axis=1, inplace=True)
df.drop('cubic_area_per_room_mean', axis=1, inplace=True)

df.to_csv(r'C:\Users\User\Desktop\household_sensors\er_7el.csv', index=False)

