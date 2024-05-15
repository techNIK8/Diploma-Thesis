"""
@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\merged_numeric_hot_months.csv')

df['many_externalwindows'] = df['externalwindows'].apply(lambda x: 1 if x > df['externalwindows'].mean() else 0)

df['high_electric_consumption'] = df['electric_con_per_hot_months_mean'].apply(lambda x: 1 if x > df['electric_con_per_hot_months_mean'].mean() else 0)

df.drop('homeid', axis=1, inplace=True)
df.drop('externalwindows', axis=1, inplace=True)
df.drop('electric_con_per_hot_months_mean', axis=1, inplace=True)
df.drop('temperature_per_hot_months_mean', axis=1, inplace=True)
df.drop('number_of_rooms', axis=1, inplace=True)

df.to_csv(r'C:\Users\User\Desktop\household_sensors\er_3el.csv', index=False)

