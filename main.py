
# importing necessary libraries
import pandas as pd
import numpy as np
from pathlib import Path
from settings.main import env_info
from utils.utils import magic, show_current_info

def main():

    # defining the variables
    min_player = env_info.min_player
    max_player = env_info.max_player
    target_batting_power = env_info.target_batting_power 
    target_bowling_power = env_info.target_bowling_power 
    current_batting_power = env_info.current_batting_power
    current_bowling_power = env_info.current_bowling_power
    remaining_balance = env_info.remaining_balance
    remaining_d_cat_balance = env_info.remaining_d_cat_balance
    players_in_team = env_info.players_in_team
    no_of_D_catagory_players = env_info.no_of_D_catagory_players
    no_of_ABC_catagory_players = env_info.no_of_ABC_catagory_players

    # Loading player data
    filepath = Path(__file__).parents[0].joinpath('Player_list.json')
    player_info = pd.read_json('Player_list.json', orient='index')
    player_info.Batting = player_info.Batting.astype(int)
    player_info.Bowling = player_info.Bowling.astype(int)
    player_info = player_info.set_index('Player No')


    total_players = 51
    for i in range(total_players):
        edit_mode = str(input('Enter edit mode : (y/n) '))
        if edit_mode not in ['y','n']:
            edit_mode = str(input('Wrong input. Enter edit mode : (y/n) '))
        edit_mode = True if edit_mode == 'y' else False
        if edit_mode is True:
            remaining_balance = int(input('Remaining balance : '))
            remaining_d_cat_balance = int(input('Remaining D-Cat balance : '))
            current_batting_power = int(input('Current batting power : '))
            current_bowling_power = int(input('Current_bowling_power : '))
            no_of_D_catagory_players = int(input('Number of D-Cat player to be bought: '))
            players_in_team = int(input('Current number of players in the team : '))
        
        player_no = int(input('Please enter the player no : '))
        show_current_info(player_no, player_info, players_in_team, current_batting_power, current_bowling_power, remaining_balance, remaining_d_cat_balance)
        print(f'\tSuggested price is : Basic -> {magic(remaining_balance, remaining_d_cat_balance, player_no, current_batting_power, current_bowling_power, players_in_team, target_batting_power, target_bowling_power, no_of_D_catagory_players, player_info)}')
        print(f'\tSuggested price is : Max -> {remaining_balance-(8-players_in_team)}\n')
        sold_status = str(input('Sold to our team?(y/n) '))
        if sold_status not in ['y','n']:
            sold_status = str(input('Wrong input. Sold to our team?(y/n) '))
        sold_status = True if sold_status == 'y' else False

        if sold_status is True:
            sold_price = int(input('Please enter the price: '))
            if sold_price != 0:
                flag = str(input('Is he one of the D group : (y/n) '))
                if flag not in ['y','n']:
                    flag = str(input('Wrong input. Is he one of the D group : (y/n) '))
                if flag == 'y':
                    remaining_d_cat_balance = remaining_d_cat_balance - sold_price
                    no_of_D_catagory_players = no_of_D_catagory_players - 1
                    current_batting_power = current_batting_power + player_info.iloc[player_no-1].Batting
                    current_bowling_power = current_bowling_power + player_info.iloc[player_no-1].Bowling
                    players_in_team = players_in_team + 1
                    print(f'\tPlayers to be bought in D cat : {no_of_D_catagory_players}')
                    
                    if no_of_D_catagory_players == 0:
                        print('Done')
                        remaining_balance = remaining_balance + remaining_d_cat_balance
                        remaining_d_cat_balance = 0
                else: 
                    remaining_balance = remaining_balance - sold_price
                    current_batting_power = current_batting_power + player_info.iloc[player_no-1].Batting
                    current_bowling_power = current_bowling_power + player_info.iloc[player_no-1].Bowling
                    players_in_team = players_in_team + 1
                    if remaining_balance < 0:
                        remaining_d_cat_balance = remaining_d_cat_balance + remaining_balance
                        remaining_balance = 0

        else:
            continue
        if i == (total_players-1):
            show_current_info(player_no, player_info, players_in_team, current_batting_power, current_bowling_power, remaining_balance, remaining_d_cat_balance)
        
if __name__ == '__main__':
    main()