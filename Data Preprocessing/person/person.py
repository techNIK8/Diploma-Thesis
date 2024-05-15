"""
Delete of rows where primaryparticipant = 0 and fill empty values with mean
@author: Nikos Kosioris
"""

import pandas as pd

df = pd.read_csv(r'C:\Users\User\Desktop\household_sensors\person.csv', usecols = ['homeid', 'education', 'weeklyhoursofwork', 'ageleavingeducation', 'primaryparticipant'])

df.drop(df.loc[df['primaryparticipant'] == 0].index, inplace=True)
df['weeklyhoursofwork'] = df['weeklyhoursofwork'].fillna('31-40')
df['education'] = df['education'].fillna('Degree level qualification (or equivalent), e.g. BSc, BA, MSc, MA')
df['ageleavingeducation'] = df['ageleavingeducation'].fillna(22)
df['ageleavingeducation'] = df['ageleavingeducation'].astype('int')
df.drop('primaryparticipant', axis=1, inplace=True)

df.to_csv(r'C:\Users\User\Desktop\household_sensors\final_person.csv', index = None)


