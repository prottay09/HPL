from pydantic import BaseSettings
import yaml
from pathlib import Path

class info(BaseSettings):
    "General info of the program"

    min_player : int
    max_player : int
    min_foreign_player : int
    max_foreign_player : int
    target_batting_power : int
    target_bowling_power : int
    current_batting_power : int
    current_bowling_power : int
    total_players : int
    total_foreign_players : int
    remaining_balance : int
    remaining_d_cat_balance : int
    players_in_team : int
    no_of_D_catagory_players : int
    no_of_ABC_catagory_players : int

# load .yaml file
#print(Path(__file__).parents[0].joinpath('info.yaml'))
with open(Path(__file__).parents[0].joinpath('info.yaml'), 'r') as stream:
    try:
        settings = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

env_info = info(**settings)