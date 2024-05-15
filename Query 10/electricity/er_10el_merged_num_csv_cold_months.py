"""
@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\merged_numeric_cold_months.csv')

df['high_cubic_area_for_clothesdrying_percent'] = df['cubic_area_for_clothesdrying_percent'].apply(lambda x: 1 if x > df['cubic_area_for_clothesdrying_percent'].mean() else 0)

df['high_electric_consumption'] = df['electric_con_per_cold_months_mean'].apply(lambda x: 1 if x > df['electric_con_per_cold_months_mean'].mean() else 0)

df.drop('homeid', axis=1, inplace=True)
df.drop('electric_con_per_cold_months_mean', axis=1, inplace=True)
df.drop('cubic_area_for_clothesdrying_percent', axis=1, inplace=True)
df.drop('temperature_per_cold_months_mean', axis=1, inplace=True)
df.drop('number_of_rooms', axis=1, inplace=True)

df.to_csv(r'C:\Users\User\Desktop\household_sensors\er_10el.csv', index=False)

