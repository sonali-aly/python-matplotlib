#import matplotlib.pyplot as plt
from matplotlib import pyplot as plt
import numpy as np

x=np.array([10,20,30,40,50])
y=np.array([20,30,12,15,20])
x1=np.array([10,20,30,40,50])
y1=np.array([10,15,14,17,22])

plt.plot(x,y,x1,y1,color="blue",linewidth='2.5',linestyle='-')
plt.xlabel("year")
plt.ylabel("pass percentages")
plt.title("pass percentages")
plt.show()
