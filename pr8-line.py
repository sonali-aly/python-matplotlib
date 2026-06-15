import matplotlib.pyplot as plt
years = [2010, 2011, 2012, 2013, 2014, 2015, 2016]
team1_performance = [85, 90, 78, 92, 95, 87, 93]
team2_performance = [78, 82, 88, 85, 90, 92, 87]  
fig, ax = plt.subplots()
ax.plot(years, team1_performance, label='Team 1', marker='o', linestyle='-', color='blue')
ax.plot(years, team2_performance, label='Team 2', marker='s', linestyle='--', color='green')
ax.set_xlabel('Year')
ax.set_ylabel('Performance Score')
ax.set_title('Cricket Team Performance Over Time')
ax.legend()
plt.grid(True)
plt.show()
