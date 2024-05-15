"""
@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\merged_numeric_cold_months.csv')

df['many_electricheaters_electric'] = df['electricheater_electric'].apply(lambda x: 1 if x > df['electricheater_electric'].mean() else 0)
df['many_electric_heaters'] = df['electric_heater'].apply(lambda x: 1 if x > df['electric_heater'].mean() else 0)
df['many_electric_heaters'] = df['many_electric_heaters'] | df['many_electricheaters_electric']

df['high_gas_pulse_consumption'] = df['gas_pulse_per_cold_months_mean'].apply(lambda x: 1 if x > df['gas_pulse_per_cold_months_mean'].mean() else 0)

df.drop('homeid', axis=1, inplace=True)
df.drop('gas_pulse_per_cold_months_mean', axis=1, inplace=True)
df.drop('temperature_per_cold_months_mean', axis=1, inplace=True)
df.drop('many_electricheaters_electric', axis=1, inplace=True)
df.drop('electricheater_electric', axis=1, inplace=True)
df.drop('electric_heater', axis=1, inplace=True)
df.drop('number_of_rooms', axis=1, inplace=True)

df.to_csv(r'C:\Users\User\Desktop\household_sensors\er_14gas.csv', index=False)

