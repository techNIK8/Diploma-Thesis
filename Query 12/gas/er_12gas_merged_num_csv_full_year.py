"""
@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\merged_numeric_full_year.csv')

df['many_residents'] = df['residents'].apply(lambda x: 1 if x > df['residents'].mean() else 0)

#df['many_residents'] = df['residents'].apply(lambda x: True if x == 12  else False)

df['high_gas_pulse_consumption'] = df['gas_pulse_per_full_year_mean'].apply(lambda x: 1 if x > df['gas_pulse_per_full_year_mean'].mean() else 0)

df.drop('homeid', axis=1, inplace=True)
df.drop('residents', axis=1, inplace=True)
df.drop('gas_pulse_per_full_year_mean', axis=1, inplace=True)
df.drop('temperature_per_full_year_mean', axis=1, inplace=True)
df.drop('number_of_rooms', axis=1, inplace=True)

df.to_csv(r'C:\Users\User\Desktop\household_sensors\er_12gas.csv', index=False)

