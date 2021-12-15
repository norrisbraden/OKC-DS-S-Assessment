
import pandas as pd
import numpy as np
import math

df = pd.read_csv('team-a.csv')

fg_made = df["fgmade"] == 1

# print(len(df[fg_made]))

# 105 FGs Made


# Corner 3 Equation
attempted_corner3 = ((df['x'] <= -22.0) | (df['x'] >= 22.0)) & (df['y'] <= 7.8)
madecorner3 = ((df['x'] <= -22.0) | (df['x'] >= 22.0)) & (df['y'] <= 7.8) & (df['fgmade'] == 1)




# Non Corner 3 Equation
df['x'] = df['x'].astype(np.float64)
df['y'] = df['y'].astype(np.float64)
madenoncorner3 = (np.sqrt(df['x']**2 + df['y']**2) >= 23.5) & (df['y'] >= 7.8) & (df['fgmade'] == 1)
attempted_noncorner3 = (np.sqrt(df['x']**2 + df['y']**2) >= 23.5) & (df['y'] >= 7.8)




#2 Pt Equation
made2pt = ((np.sqrt(df['x']**2 + df['y']**2) < 23.5) & (df['y'] > 7.8)) & (df['fgmade'] == 1) | (np.sqrt(df['x']**2 + df['y']**2) < 22) & (df['y'] < 7.8) & (df['fgmade'] == 1)
attempted_2pt = ((np.sqrt(df['x']**2 + df['y']**2) < 23.5) & (df['y'] > 7.8)) | (np.sqrt(df['x']**2 + df['y']**2) < 22) & (df['y'] < 7.8)


# Percentages
# 280 Total Attempts

print(len(df[madecorner3])) # 8
print(len(df[attempted_corner3])) #20

print(len(df[madenoncorner3])) #29
print(len(df[attempted_noncorner3])) #90

print(len(df[made2pt])) #68
print(len(df[attempted_2pt])) #170

fgattempted = 280

#PERCENTAGE BASED ON ZONE

percentcorner3 = (len(df[attempted_corner3]) / fgattempted) * 100
print(percentcorner3)


percent_noncorner3 = (len(df[attempted_noncorner3]) / fgattempted) * 100
print(percent_noncorner3)


percent_2pt = (len(df[attempted_2pt]) / fgattempted) * 100
print(percent_2pt)


# EFFECTIVE FG PERCENTAGE BY ZONE

efg_noncorner3 = (((len(df[madenoncorner3]) * .5) + len(df[madenoncorner3])) / len(df[attempted_noncorner3])) * 100
print(efg_noncorner3)

efg_corner3 = (((len(df[madecorner3]) * .5) + len(df[madecorner3])) / len(df[attempted_corner3])) * 100
print(efg_corner3)

efg_2pt = (len(df[made2pt]) / len(df[attempted_2pt])) * 100
print(efg_2pt)


