import pandas as pd

# Load the "football.csv" dataset into a dataframe called "foot_ball"
foot_ball = pd.read_csv("football.csv")


foot_ball.tail(7)


nationality_and_club = foot_ball[["Nationality", "Club"]]
print(nationality_and_club.head())


tenth_player_data = foot_ball.iloc[9]
print(tenth_player_data)


goals_appearances_subset = foot_ball.loc[100:110, ["Goals", "Appearances"]]
print(goals_appearances_subset)


foot_ball["Goals per Appearance"] = foot_ball["Goals"] / foot_ball["Appearances"]
print(foot_ball.head())


arsenal_players = foot_ball[foot_ball["Club"] == "Arsenal"]
print(arsenal_players)


high_scorers = foot_ball[foot_ball["Goals"] > 5]
print(high_scorers)


pip install --upgrade pandas