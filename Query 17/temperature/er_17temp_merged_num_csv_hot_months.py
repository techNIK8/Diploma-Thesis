"""
@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\merged_numeric_hot_months.csv')

df['many_electric_fans'] = df['electric_fan'].apply(lambda x: 1 if x > df['electric_fan'].mean() else 0)
df['many_air_conditioning'] = df['air_conditioning'].apply(lambda x: 1 if x > df['air_conditioning'].mean() else 0)
df['many_air_conditioning_fans'] = df['many_electric_fans'] | df['many_air_conditioning']

df['low_temperature'] = df['temperature_per_hot_months_mean'].apply(lambda x: 1 if x < df['temperature_per_hot_months_mean'].mean() else 0)

df.drop('homeid', axis=1, inplace=True)
df.drop('temperature_per_hot_months_mean', axis=1, inplace=True)
df.drop('many_air_conditioning', axis=1, inplace=True)
df.drop('many_electric_fans', axis=1, inplace=True)
df.drop('electric_fan', axis=1, inplace=True)
df.drop('air_conditioning', axis=1, inplace=True)
df.drop('number_of_rooms', axis=1, inplace=True)

df.to_csv(r'C:\Users\User\Desktop\household_sensors\er_17temp.csv', index=False)

