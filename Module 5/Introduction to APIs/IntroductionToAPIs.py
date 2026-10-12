from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd

def one_dict(list_dict):
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict

print("Head of the dataframe of the NBA teams")
nba_teams_df = pd.DataFrame(one_dict(teams.get_teams()))
print(nba_teams_df.head())

print("\nDataframe of the NBA teams filtered by the column 'nickname' as 'Warriors'")
warriors_df = nba_teams_df[nba_teams_df['nickname'] == 'Warriors']
print(warriors_df)
