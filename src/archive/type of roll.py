from src.helper_functions import *


dirpath = '/home/o/Downloads/Galv/capstone1/Mighty-Rolls/data/All Rolls - Wildemount/'
df = html_to_df(dirpath).dropna(subset=['Episode'])
col = 'Type of Roll'
print_info(df, col)

# Not d20 rolls: Other, Damage, Fragment, Percentage, Unknown,
d20_filter_out_list = ['Other', 'Damage', 'Fragment', 'Percentage', 'Unknown', 'Hit Dice']
df = remove_rows(df, col, d20_filter_out_list)

print_info(df, col)












