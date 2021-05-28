import pandas as pd

def magic(
    remaining_balance : int,
    remaining_d_cat_balance : int,
    player_no : int,
    current_batting_power : int,
    current_bowling_power : int,
    players_in_team : int,
    target_batting_power : int,
    target_bowling_power : int,
    no_of_D_catagory_players : int,
    player_info : pd.DataFrame
)->int:

    batting_power_needed = target_batting_power - current_batting_power
    bowling_power_needed = target_bowling_power - current_bowling_power
    # batting_budget = remaining_balance * (batting_power_needed/(batting_power_needed+bowling_power_needed))
    # bowling_budget = remaining_balance * (bowling_power_needed/(batting_power_needed+bowling_power_needed))
    # suggested_price = (batting_budget * (int(player_info.iloc[player_no-1].Batting)/batting_power_needed)) + (bowling_budget * (int(player_info.iloc[player_no-1].Bowling)/bowling_power_needed))
    if player_info.iloc[player_no-1].Batting > batting_power_needed:
        print('\tBatting overpowered')
    if player_info.iloc[player_no-1].Bowling > bowling_power_needed:
        print('\tBowling overpowered')
    if (int(player_info.iloc[player_no-1].Batting)+ int(player_info.iloc[player_no-1].Bowling)) < 3:
        suggested_price = 300
        print('\tD catagory player')
    elif remaining_balance == 0:
        print('You don''t have enough balance')
        suggested_price = 0
    else:
        avg_batting_star =  batting_power_needed / (9-players_in_team-no_of_D_catagory_players)
        avg_bowling_star = bowling_power_needed / (9-players_in_team-no_of_D_catagory_players)
        avg_price = remaining_balance/(9-players_in_team-no_of_D_catagory_players)
        avg_price_bat = avg_price*(avg_batting_star/(avg_batting_star+avg_bowling_star))
        #print(avg_price_bat)
        avg_price_bowl = avg_price*(avg_bowling_star/(avg_batting_star+avg_bowling_star))
        #print(avg_price_bowl)
        suggested_price = avg_price_bat*(int(player_info.iloc[player_no-1].Batting)/avg_batting_star) + avg_price_bowl*(int(player_info.iloc[player_no-1].Bowling)/avg_bowling_star) 
        
    if suggested_price > remaining_balance & players_in_team == 8:
        suggested_price = remaining_balance
    if remaining_balance-suggested_price < (9-players_in_team-no_of_D_catagory_players-1)*400:
        suggested_price = remaining_balance - (9-players_in_team-no_of_D_catagory_players-1)*400
        print('He is a good player but your balance is insufficient, Think!')
        print(f'You have to buy {9-players_in_team} players with {remaining_balance+remaining_d_cat_balance}')
    
    return suggested_price


def show_current_info(
    player_no : int,
    player_info : pd.DataFrame,
    players_in_team : int,
    current_batting_power : int,
    current_bowling_power : int,
    remaining_balance : int,
    remaining_d_cat_balance : int
)->None:
    print('************************************')
    print(f'Current batting power : {current_batting_power}')
    print(f'Current bowling power : {current_bowling_power}')
    print(f'Total players in the team : {players_in_team}')
    print(f'Remaining balance : {remaining_balance}\n')
    print(f'Remaining D-CAT balance : {remaining_d_cat_balance}\n')
    print(f'\tPlayer No : {player_no}')
    print(f'\tPlayer name : {player_info.iloc[player_no-1].Name}')
    print(f'\tBatting : {player_info.iloc[player_no-1].Batting}')
    print(f'\tBowling : {player_info.iloc[player_no-1].Bowling}')
