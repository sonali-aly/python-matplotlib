import matplotlib.pyplot as plt
years = ['2020`', '2021', '2022', '2023', '2024']
percentages = [80, 85, 88, 92, 95]
colors = ['royalblue', 'forestgreen', 'orangered', 'mediumpurple', 'gold']
plt.bar(years, percentages, color=colors)
plt.xlabel('Year')
plt.ylabel('Percentage of Students')
plt.title('Percentage of Students Over the Last Five Years')
plt.show()
