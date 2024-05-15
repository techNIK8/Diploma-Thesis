"""
@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\merged_numeric_winter_time-summer_time.csv')

df['high_gas_pulse_consumption'] = df['gas_pulse_mean'].apply(lambda x: 1 if x > df['gas_pulse_mean'].mean() else 0)

df.drop('homeid', axis=1, inplace=True)
df.drop('gas_pulse_mean', axis=1, inplace=True)
df.drop('number_of_rooms', axis=1, inplace=True)

df.to_csv(r'C:\Users\User\Desktop\household_sensors\er_18gas.csv', index=False)

