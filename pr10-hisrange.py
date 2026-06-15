import matplotlib.pyplot as plt
data = [68, 74, 82, 79, 92, 85, 88, 78, 90, 84, 74, 82, 95, 86, 80, 89, 92, 75, 81, 93]
plt.hist(data, bins=5, range=(70, 90), edgecolor='k')
plt.title('Exam Scores Histogram')
plt.xlabel('Score Range')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
