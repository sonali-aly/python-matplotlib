import matplotlib.pyplot as plt
import numpy as np
categories = ['Category A', 'Category B', 'Category C', 'Category D']
values1 = [15, 30, 45, 10]
values2 = [10, 25, 35, 5]
bar_width = 0.4  
y_pos = np.arange(len(categories))
fig, ax = plt.subplots()
ax.barh(y_pos - bar_width/2, values1, height=bar_width, label='Set 1', color='b')
ax.barh(y_pos + bar_width/2, values2, height=bar_width, label='Set 2', color='g')
ax.set_yticks(y_pos)
ax.set_yticklabels(categories)
ax.set_xlabel('Values')
ax.set_title('Multiple Horizontal Bars')
ax.legend()
plt.show()
