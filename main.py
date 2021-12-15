import pandas as pd
import math

df = pd.read_csv('shots_data.csv')

# seperating teams
team_a = df[(df['team'] == 'Team A')]
# exporting teams to separate csv files
team_a.to_csv('team-a.csv')

#creating new team b csv
team_b = df[(df['team'] == 'Team B')]

team_b.to_csv('team-b.csv')

