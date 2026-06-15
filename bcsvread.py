import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')
selected_columns = ['year', 'wheat', 'gram']
df_selected = df[selected_columns]
bar_width = 0.35
index = df_selected.index
plt.bar(index, df_selected['wheat'], bar_width, label='wheat')
plt.bar(index + bar_width, df_selected['gram'], bar_width, label='gram')
plt.xlabel('year')
plt.ylabel('Quantity')
plt.title('food production')
plt.xticks(index + bar_width / 2, df_selected['year'])
plt.legend()
plt.show()
