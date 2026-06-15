import matplotlib.pyplot as plt
import numpy as np
y=np.array(["wheat","gram","rice","pulses"])
x=np.array([200,300,150,500])
n=4
r=np.arange(n)
width=0.25
plt.bar(r,x,color='b',width=width,edgecolor='black',label='food')
plt.bar(r+width,y,color='g',width=width,edgecolor='black',label='tons')
plt.xlabel("Food items")
plt.ylabel("production")
plt.title("Food Production in India in 2023")
plt.bar(x,y)
plt.xticks(r+width/2,['2019','2020','2021','2022'])
plt.legend()
plt.show()
