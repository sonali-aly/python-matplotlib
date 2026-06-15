import matplotlib.pyplot as plt
labels = ['BJP', 'Congree', 'AAP', 'Others']
sizes = [25, 30, 15, 30]
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.axis('equal')  
plt.title('Distribution of Categories')
plt.show()
