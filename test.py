import pandas as pd
df = pd.read_json('Player_list.json', orient='index')
print(df.iloc[0])