import matplotlib.pyplot as plt
import numpy as np
x = [12,23,34]
y1 = [23,33,45]
y2 = [12,26,67]
y3 = [1,2,3]
y4 = [6,7,8]
fig, axes = plt.subplots(2, 2, figsize=(10, 8))
axes[0, 0].plot(x, y1)
axes[0, 0].set_title('pppp')
axes[0, 1].plot(x, y2)
axes[0, 1].set_title('oooo')
axes[1, 0].plot(x, y3)
axes[1, 0].set_title('uuuu')
axes[1, 1].plot(x, y4)
axes[1, 1].set_title('tttt')
plt.tight_layout()
plt.show()
