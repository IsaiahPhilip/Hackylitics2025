#Imports 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import zipfile
import os

# Read Data
zip_filename = "NBA_2024_Shots.zip"
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
data_dir = os.path.join(parent_dir, "data")
zip_path = os.path.join(data_dir, zip_filename)

# zip_file_path = "/Users/aaronchanner/Desktop/Hackylitics2025/basketball-app/data/NBA_2024_Shots.zip"
# path_to_data_folder = "/Users/aaronchanner/Desktop/Hackylitics2025/basketball-app/data"
csv_file_name = "NBA_2024_Shots 2.csv"
with zipfile.ZipFile(zip_path,'r') as zip_ref:
    zip_ref.extractall(data_dir)

csv_path = os.path.join(data_dir, csv_file_name)
data = pd.read_csv(csv_path)
data[['LOC_X', 'LOC_Y']] = data[['LOC_X', 'LOC_Y']].round()

x_coord = data.iloc[:,20]
y_coord = data.iloc[:,21]


rounded_x_coord = np.round(x_coord)
rounded_y_coord = np.round(y_coord)
# plt.scatter(rounded_y_coord, rounded_x_coord)
# plt.xlim(0, 100)
# plt.ylim(-25, 25)
# plt.show()

coords = data.loc[:, ['GAME_ID','SHOT_MADE','LOC_X', 'LOC_Y']].round()
# print(coords)

def point_shot(x_coord, y_coord):
    try:
        ## find all shots taken from that point
        shots_at_coord = coords[(coords['LOC_X'] == x_coord) & (coords['LOC_Y'] == y_coord)]
        ## calculate all shots made from that point
        shots_made_at_coord = shots_at_coord[(shots_at_coord['SHOT_MADE'] == True)]
        ## divide shots made by total shots and return percentage
        return len(shots_made_at_coord)/len(shots_at_coord)
    except ZeroDivisionError:
        return pd.NA

#print(point_shot(4, 35))

#debug cell
# coords2 = data.loc[:, ['GAME_ID','SHOT_MADE','LOC_X', 'LOC_Y']].round() 

# for x in range(-25,25):
#     for y in range(0,100):
#         shots_at_coord = coords2[(coords2['LOC_X'] == x) & (coords2['LOC_Y'] == y)]
#         shots_made_at_coord = shots_at_coord[(shots_at_coord['SHOT_MADE'] == True)]
#         print(x,y,len(shots_at_coord),len(shots_made_at_coord),point_shot(x, y))

# Filter Functions
def team_filter(team_name):
    temp_data = data.set_index('TEAM_NAME')
    team_data = temp_data.filter(like=team_name, axis='rows')
    return team_data

def player_filter(player_name):
    temp_data = data.set_index('PLAYER_NAME')
    player_data = temp_data.filter(like=player_name, axis='rows')
    return player_data

def season_filter(season):
    temp_data = data.set_index('SEASON_2')
    season_data = temp_data.filter(like='2023-24', axis='rows')
    return season_data

# season_filter('2023-24')
#player_filter('LeBron James')
# team_filter("Detroit Pistons")

# created CSV for frontend data base to reference
write_name = "2024shotpct.csv"
write_path = os.path.join(data_dir,write_name)
unique_data = data[['SEASON_1', 'LOC_X', 'LOC_Y']].drop_duplicates(subset=['LOC_X', 'LOC_Y'])
unique_data['SHOT_PCT'] = unique_data.apply(lambda row: point_shot(row['LOC_X'], row['LOC_Y']), axis=1)

unique_data[['SEASON_1', 'LOC_X', 'LOC_Y', 'SHOT_PCT']].fillna('').to_csv(write_path, index=False)
