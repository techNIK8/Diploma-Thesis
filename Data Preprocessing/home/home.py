"""
Extract useful columns and replace missing values with the average

@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\home.csv', usecols = ['homeid','residents','income_band','urban_rural_name','build_era','occupied_days','occupied_nights'])
df['income_band'] = df['income_band'].str.replace('Missing','£54,000 to £65,999')
df.to_csv(r'C:\Users\User\Desktop\household_sensors\final_home.csv', index = None)