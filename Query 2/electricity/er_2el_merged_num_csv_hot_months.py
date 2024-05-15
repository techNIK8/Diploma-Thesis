"""
@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\merged_numeric_hot_months.csv')

df.loc[(df['education_Degree_level_qualification_or_equivalent_eg_BSc_BA_MSc_MA'] == 1) | 
           (df['education_PhD'] == 1)
           , 'high_level_education'] = 1

df['high_level_education'] = df['high_level_education'].fillna(0)
df['high_level_education'] = df['high_level_education'].astype('int')

df['high_electric_consumption'] = df['electric_con_per_hot_months_mean'].apply(lambda x: 1 if x > df['electric_con_per_hot_months_mean'].mean() else 0)

df.drop('homeid', axis=1, inplace=True)
df.drop('electric_con_per_hot_months_mean', axis=1, inplace=True)
df.drop('temperature_per_hot_months_mean', axis=1, inplace=True)
df.drop('education_A_to_Levels_or_Highers', axis=1, inplace=True)
df.drop('education_Degree_level_qualification_or_equivalent_eg_BSc_BA_MSc_MA', axis=1, inplace=True)
df.drop('education_GCSE_grade_D_to_G_or_CSE_grade_2_to_5_or_Standard_Grade_level_4_to_6', axis=1, inplace=True)
df.drop('education_Higher_educational_qualification_below_degree_level', axis=1, inplace=True)
df.drop('education_No_formal_qualifications', axis=1, inplace=True)
df.drop('education_O_Level_or_GCSE_equivalent_Grade_A_to_C_or_O_Grade_CSE_equivalent_Grade_1_or_Standard_Grade_level_1', axis=1, inplace=True)
df.drop('education_PhD', axis=1, inplace=True)
df.drop('education_Other_qualifications', axis=1, inplace=True)
df.drop('number_of_rooms', axis=1, inplace=True)

df.to_csv(r'C:\Users\User\Desktop\household_sensors\er_2el.csv', index=False)

