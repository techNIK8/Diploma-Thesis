"""
@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\merged_numeric_full_year.csv')

df['high_cubic_area_with_trvs_percent'] = df['cubic_area_with_trvs_percent'].apply(lambda x: 1 if x > df['cubic_area_with_trvs_percent'].mean() else 0)

df['high_gas_pulse_consumption'] = df['gas_pulse_per_full_year_mean'].apply(lambda x: 1 if x > df['gas_pulse_per_full_year_mean'].mean() else 0)

df.drop('homeid', axis=1, inplace=True)
df.drop('cubic_area_with_trvs_percent', axis=1, inplace=True)
df.drop('gas_pulse_per_full_year_mean', axis=1, inplace=True)
df.drop('temperature_per_full_year_mean', axis=1, inplace=True)
df.drop('number_of_rooms', axis=1, inplace=True)

df.to_csv(r'C:\Users\User\Desktop\household_sensors\er_11gas.csv', index=False)

