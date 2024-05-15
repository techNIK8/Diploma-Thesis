"""
@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\merged_numeric_full_year.csv')

df['many_openablewindows'] = df['windowsopen'].apply(lambda x: 1 if x > df['windowsopen'].mean() else 0)

df['high_electric_consumption'] = df['electric_con_per_full_year_mean'].apply(lambda x: 1 if x > df['electric_con_per_full_year_mean'].mean() else 0)

df.drop('homeid', axis=1, inplace=True)
df.drop('electric_con_per_full_year_mean', axis=1, inplace=True)
df.drop('temperature_per_full_year_mean', axis=1, inplace=True)
df.drop('windowsopen', axis=1, inplace=True)
df.drop('number_of_rooms', axis=1, inplace=True)

df.to_csv(r'C:\Users\User\Desktop\household_sensors\er_4el.csv', index=False)

