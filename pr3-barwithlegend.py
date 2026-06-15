import matplotlib.pyplot as plt
years = ['Year 1', 'Year 2', 'Year 3', 'Year 4', 'Year 5']
percentages = [80, 85, 88, 92, 95]  
colors = ['royalblue', 'forestgreen', 'orangered', 'mediumpurple', 'gold']
bars = plt.bar(years, percentages, color=colors)
for bar, year in zip(bars, years):
    bar.set_label(year)
plt.xlabel('Year')
plt.ylabel('Percentage of Students')
plt.title('Percentage of Students Over the Last Five Years')
plt.legend()
plt.show()
