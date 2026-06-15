import matplotlib.pyplot as plt
hours_studied = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
exam_scores = [50, 55, 60, 65, 70, 75, 80, 85, 90, 95]
plt.scatter(hours_studied, exam_scores, color='blue', marker='o', label='Data Points')
plt.title('Scatter Diagram of Hours Studied vs. Exam Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Exam Scores')
plt.grid(True)
plt.legend()
plt.show()
