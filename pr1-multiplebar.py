import matplotlib.pyplot as plt
import numpy as np
categories = ['2020', '2021', '2022', '2023']
wheat = [10, 15, 7, 12]
gram = [8, 10, 11, 9]
pulses = [12, 9, 8, 11]
bar_width = 0.2
index = np.arange(len(categories))
plt.bar(index, wheat, bar_width, label='wheat')
plt.bar(index + bar_width, gram, bar_width, label='gram')
plt.bar(index + 2 * bar_width, pulses, bar_width, label='pulses')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Multiple Bar Chart')
plt.xticks(index + bar_width, categories)
plt.legend()
plt.show()

