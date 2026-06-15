import matplotlib.pyplot as plt
categories = ['Category A', 'Category B', 'Category C', 'Category D']
data1 = [10, 15, 12, 8]  
data2 = [5, 12, 10, 6]  
data3 = [3, 8, 5, 4]    
fig, ax = plt.subplots()
x = range(len(categories))
ax.bar(x, data1, label='Data 1', color='r')
ax.bar(x, data2, label='Data 2', bottom=data1, color='g')
ax.bar(x, data3, label='Data 3', bottom=[data1[i] + data2[i] for i in range(len(data1))], color='b')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_ylabel('Values')
ax.set_title('Stacked Bar Chart')
ax.legend()
plt.show()
