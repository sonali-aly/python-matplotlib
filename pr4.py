#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import numpy as np

x=np.array([2020,2021,2022,2023])
y=np.array([90,50,80,75])
plt.plot(x,y,'ys:')
plt.xlabel("year")
plt.ylabel("pass percentages")
plt.title("pass percentages")
plt.show()
