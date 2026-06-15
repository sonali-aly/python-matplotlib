#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import numpy as np

x=np.array([2020,2021,2022,2023])
y=np.array([90,50,80,75])
plt.plot(x,y,color="r",linewidth='2.5',linestyle='solid')
plt.xlabel("year")
plt.ylabel("pass percentages")
plt.title("result")
plt.show()
