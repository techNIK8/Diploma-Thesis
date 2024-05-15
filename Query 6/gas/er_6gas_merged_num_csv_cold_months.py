"""
@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\merged_numeric_cold_months.csv')

df['many_externalwalls'] = df['externalwalls'].apply(lambda x: 1 if x > df['externalwalls'].mean() else 0)

df['high_gas_pulse_consumption'] = df['gas_pulse_per_cold_months_mean'].apply(lambda x: 1 if x > df['gas_pulse_per_cold_months_mean'].mean() else 0)

df.drop('homeid', axis=1, inplace=True)
df.drop('externalwalls', axis=1, inplace=True)
df.drop('gas_pulse_per_cold_months_mean', axis=1, inplace=True)
df.drop('temperature_per_cold_months_mean', axis=1, inplace=True)
df.drop('number_of_rooms', axis=1, inplace=True)

df.to_csv(r'C:\Users\User\Desktop\household_sensors\er_6gas.csv', index=False)

