"""
Merge all processed csv files by homeid

@author: Nikos Kosioris
"""

import pandas as pd
  
#read csv files
data1 = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\final_home.csv')
data2 = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\final_person.csv')
data3 = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\final_room.csv')
data4 = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\final_appliance.csv')
data5 = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\final_other_appliance.csv')
data6 = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\final_tariff.csv')
data7 = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\final_mean_electric-mains_electric-combined_winter_time.csv')
data8 = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\final_mean_pulse_gas_winter_time.csv')
data9 = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\final_mean_light_winter_time.csv') 
data10 = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\final_mean_electric-mains_electric-combined_summer_time.csv')
data11 = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\final_mean_pulse_gas_summer_time.csv') 
data12 = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\final_mean_light_summer_time.csv') 

#use merge function by setting how = 'outer'
output = pd.merge(data1, data2, on='homeid', how='outer')
output = pd.merge(output, data3, on='homeid', how='outer')
output = pd.merge(output, data4, on='homeid', how='outer')
output = pd.merge(output, data5, on='homeid', how='outer')
output = pd.merge(output, data6, on='homeid', how='outer')
output_winter_time = pd.merge(output, data7, on='homeid', how='outer')
output_winter_time = pd.merge(output_winter_time, data8, on='homeid', how='outer')
output_winter_time = pd.merge(output_winter_time, data9, on='homeid', how='outer')

output_winter_time['winter_time'] = True

output_summer_time = pd.merge(output, data10, on='homeid', how='outer')
output_summer_time = pd.merge(output_summer_time, data11, on='homeid', how='outer')
output_summer_time = pd.merge(output_summer_time, data12, on='homeid', how='outer')

output_summer_time['winter_time'] = False

frames = [output_winter_time, output_summer_time]

output = pd.concat(frames)

output['electric_con_per_winter_time_mean'] = output['electric_con_per_winter_time_mean'].fillna(output.pop('electric_con_per_summer_time_mean'))
output['gas_pulse_per_winter_time_mean'] = output['gas_pulse_per_winter_time_mean'].fillna(output.pop('gas_pulse_per_summer_time_mean'))
output['light_per_winter_time_mean'] = output['light_per_winter_time_mean'].fillna(output.pop('light_per_summer_time_mean'))

output.rename(columns={'electric_con_per_winter_time_mean': 'electric_con_mean', 'gas_pulse_per_winter_time_mean': 'gas_pulse_mean', 'light_per_winter_time_mean': 'light_mean'}, inplace=True)


unit_charge_pence_per_kwh_gas_mean = output['unit_charge_pence_per_kwh_gas'].mean()
output['unit_charge_pence_per_kwh_gas'].fillna(value=unit_charge_pence_per_kwh_gas_mean, inplace=True)   #replace empty values with mean value
output.loc[output['unit_charge_pence_per_kwh_gas'] < 1, 'unit_charge_pence_per_kwh_gas'] = unit_charge_pence_per_kwh_gas_mean    #replace outliers (< 1) with mean value
output['unit_charge_pence_per_kwh_gas'] = output['unit_charge_pence_per_kwh_gas'].round(decimals = 2)

unit_charge_pence_per_kwh_electric_mean = output['unit_charge_pence_per_kwh_electricity'].mean()
output['unit_charge_pence_per_kwh_electricity'].fillna(value=unit_charge_pence_per_kwh_electric_mean, inplace=True)   #replace empty values with mean value
output.loc[output['unit_charge_pence_per_kwh_electricity'] < 1, 'unit_charge_pence_per_kwh_electricity'] = unit_charge_pence_per_kwh_gas_mean    #replace outliers (< 1) with mean value
output['unit_charge_pence_per_kwh_electricity'] = output['unit_charge_pence_per_kwh_electricity'].round(decimals = 2)

#list with homeids which do not qualify the criteria (not enough data)
values = [47, 61, 80, 82, 84, 86, 126, 143, 156, 171, 173, 192, 210, 254, 267, 272, 
          282, 288, 293, 306, 308, 307, 308, 309, 310, 311, 313, 315, 316, 317, 
          318, 319, 320, 321, 322, 323, 325, 326, 327, 328, 329, 330, 331, 332, 
          333, 334, 335, 223, 305]

output = output[output.homeid.isin(values) == False]   #drop any rows that have values from the list in the homeid column

output.to_csv(r'C:\Users\User\Desktop\household_sensors\merged_winter_time-summer_time.csv', index=False)