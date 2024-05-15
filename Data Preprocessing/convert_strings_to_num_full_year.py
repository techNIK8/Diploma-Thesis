"""
Convert non-numeric data to numeric
Need to run merged_*.py after

@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\merged_full_year.csv')

df['income_band'] = df['income_band'].str.replace('less than £10,800','9449.5')
df['income_band'] = df['income_band'].str.replace('£10,800 to £13,499','12149.5')
df['income_band'] = df['income_band'].str.replace('£13,500 to £16,199','14849.5')
df['income_band'] = df['income_band'].str.replace('£16,200 to £19,799','17999.5')
df['income_band'] = df['income_band'].str.replace('£19,800 to £23,399','21599.5')
df['income_band'] = df['income_band'].str.replace('£23,400 to £26,999','25199.5')
df['income_band'] = df['income_band'].str.replace('£27,000 to £32,399','29699.5')
df['income_band'] = df['income_band'].str.replace('£32,400 to £37,799','35099.5')
df['income_band'] = df['income_band'].str.replace('£37,800 to £43,199','40499.5')
df['income_band'] = df['income_band'].str.replace('£43,200 to £48,599','45899.5')
df['income_band'] = df['income_band'].str.replace('£48,600 to £53,999','51299.5')
df['income_band'] = df['income_band'].str.replace('£54,000 to £65,999','59999.5')
df['income_band'] = df['income_band'].str.replace('£66,000 to £77,999','71999.5')
df['income_band'] = df['income_band'].str.replace('£78,000 to £89,999','83999.5')
df['income_band'] = df['income_band'].str.replace('£90,000 or more','95999.5')
df['income_band'] = df['income_band'].astype(float)

df['build_era'] = df['build_era'].str.replace('Before 1850','1825')
df['build_era'] = df['build_era'].str.replace('1850-1899','1874')
df['build_era'] = df['build_era'].str.replace('1900-1918','1909')
df['build_era'] = df['build_era'].str.replace('1919-1930','1924')
df['build_era'] = df['build_era'].str.replace('1931-1944','1937')
df['build_era'] = df['build_era'].str.replace('1945-1964','1954')
df['build_era'] = df['build_era'].str.replace('1965-1980','1972')
df['build_era'] = df['build_era'].str.replace('1981-1990','1985')
df['build_era'] = df['build_era'].str.replace('1991-1995','1993')
df['build_era'] = df['build_era'].str.replace('1996-2001','1998')
df['build_era'] = df['build_era'].str.replace('2002 or later','2004')
df['build_era'] = df['build_era'].astype(int)

df['weeklyhoursofwork'] = df['weeklyhoursofwork'].str.replace('+','', regex = True) 
df['weeklyhoursofwork'] = df['weeklyhoursofwork'].str.replace('1-10','5')
df['weeklyhoursofwork'] = df['weeklyhoursofwork'].str.replace('11-20','15')
df['weeklyhoursofwork'] = df['weeklyhoursofwork'].str.replace('21-30','25')
df['weeklyhoursofwork'] = df['weeklyhoursofwork'].str.replace('31-40','35')
df['weeklyhoursofwork'] = df['weeklyhoursofwork'].str.replace('41-50','45')
df['weeklyhoursofwork'] = df['weeklyhoursofwork'].str.replace('51+','55', regex = True) 
df['weeklyhoursofwork'] = df['weeklyhoursofwork'].astype(int)

df['urban_rural_name'] = df['urban_rural_name'].str.replace(' ','_', regex = True)
urban_rural_name = pd.get_dummies(df.urban_rural_name, prefix='urban_rural_name')
urban_rural_name = urban_rural_name.astype(int) 

df['education'] = df['education'].str.replace('-',' to ', regex = True) 
df['education'] = df['education'].str.replace('/','_', regex = True) 
df['education'] = df['education'].str.replace('(','', regex = True) 
df['education'] = df['education'].str.replace(')','', regex = True)
df['education'] = df['education'].str.replace('.','', regex = True)
df['education'] = df['education'].str.replace(',','', regex = True)
df['education'] = df['education'].str.replace(' ','_', regex = True)
 
education = pd.get_dummies(df.education, prefix='education')
education.rename(columns = {'education_No_formal_qualifications_':'education_No_formal_qualifications'}, inplace = True)
education = education.astype(int)

df.drop('urban_rural_name', axis=1, inplace=True)
df.drop('education', axis=1, inplace=True)

df = pd.merge(df, urban_rural_name, left_index=True, right_index=True)
df = pd.merge(df, education, left_index=True, right_index=True)

df.to_csv(r'C:\Users\User\Desktop\household_sensors\merged_numeric_full_year.csv', index = None)