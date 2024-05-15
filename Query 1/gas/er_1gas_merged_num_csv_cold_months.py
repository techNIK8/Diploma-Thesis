"""
@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\merged_numeric_cold_months.csv')

df.loc[(df['income_band'] == 51299.5) | 
           (df['income_band'] == 59999.5) |
           (df['income_band'] == 71999.5) |
           (df['income_band'] == 83999.5) |
           (df['income_band'] == 95999.5)
           , 'high_income'] = 1

df['high_income'] = df['high_income'].fillna(0)
df['high_income'] = df['high_income'].astype('int')

df['high_gas_pulse_consumption'] = df['gas_pulse_per_cold_months_mean'].apply(lambda x: 1 if x > df['gas_pulse_per_cold_months_mean'].mean() else 0)

df.drop('homeid', axis=1, inplace=True)
df.drop('gas_pulse_per_cold_months_mean', axis=1, inplace=True)
df.drop('temperature_per_cold_months_mean', axis=1, inplace=True)
df.drop('income_band', axis=1, inplace=True)
df.drop('number_of_rooms', axis=1, inplace=True)

df.to_csv(r'C:\Users\User\Desktop\household_sensors\er_1gas.csv', index=False)

