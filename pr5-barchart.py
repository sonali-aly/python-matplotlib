import matplotlib.pyplot as plt
import numpy as np
x=np.array(["wheat","gram","rice","pulses"])
y=np.array([2000,3000,1500,5000])

plt.xlabel("Food items")
plt.ylabel("production")
plt.title("Food Production in India in 2023")
plt.bar(x,y)
plt.show()
