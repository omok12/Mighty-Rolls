from src.helper_functions import *
import matplotlib.pyplot as plt
import seaborn as sns


dirpath = '/home/o/Downloads/Galv/capstone1/Mighty-Rolls/data/All Rolls - Wildemount/'

# clean Total Value feature
df = html_to_df(dirpath).dropna(subset=['Episode'])
col = 'Total Value'

d20_filter_out_list = ['Other', 'Damage', 'Fragment', 'Percentage', 'Unknown', 'Hit Dice']
df = remove_rows(df, 'Type of Roll', d20_filter_out_list)

remove_list = []
for i in range(21):
    remove_list.append('Nat'+str(i))
remove_list.append('Unknown')
df = remove_rows(df, col, remove_list)

# plot histogram
x = df[col].astype('int32')
sns.distplot(x, bins=20).set_title('Total Value Histogram')
plt.show()

