"""
Calculate average kwh and gas pulse per homeid

@author: Nikos Kosioris
"""

import pandas as pd

df_tariff_1 = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\tariff.csv')
df_tariff_2 = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\tariff.csv')


df_tariff_1.drop(df_tariff_1.loc[df_tariff_1['energytype'] == 'electricity'].index, inplace=True)
df_new_tariff_1 = df_tariff_1.groupby(['homeid']).mean()    #calculate mean kwh per homeid
df_new_tariff_1 = df_new_tariff_1.drop('daily_standing_charge_pence', axis=1)
df_new_tariff_1.rename(columns = {'unit_charge_pence_per_kwh':'unit_charge_pence_per_kwh_gas'}, inplace = True)


df_tariff_2.drop(df_tariff_2.loc[df_tariff_2['energytype'] == 'gas'].index, inplace=True)
df_new_tariff_2 = df_tariff_2.groupby(['homeid']).mean()    #calculate mean gas pulse per homeid
df_new_tariff_2 = df_new_tariff_2.drop('daily_standing_charge_pence', axis=1)
df_new_tariff_2.rename(columns = {'unit_charge_pence_per_kwh':'unit_charge_pence_per_kwh_electricity'}, inplace = True)


output = pd.merge(df_new_tariff_1, df_new_tariff_2, on='homeid', how='outer')
output.to_csv(r'C:\Users\User\Desktop\household_sensors\final_tariff.csv')


