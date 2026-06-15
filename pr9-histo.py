import matplotlib.pyplot as plt
import numpy as np
exam_scores = [68, 74, 82, 79, 92, 85, 88, 78, 90, 84, 74, 82, 95, 86, 80, 89, 92, 75, 81, 93]
plt.hist(exam_scores, bins=7, edgecolor='k', alpha=0.7)
plt.title('Exam Scores Histogram')
plt.xlabel('Score Range')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
