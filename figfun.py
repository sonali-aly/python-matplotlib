#write a program to show the use of figure function
import matplotlib.pyplot as plt
import numpy as np
fig = plt.figure(figsize=(8, 6))
ax1 = fig.add_subplot(2, 2, 1)
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)
ax1.plot(x, y)
ax1.set_title('Sine Wave')
ax2 = fig.add_subplot(2, 2, 2)
x = np.linspace(0, 2 * np.pi, 100)
y = np.cos(x)
ax2.plot(x, y)
ax2.set_title('Cosine Wave')
ax3 = fig.add_subplot(2, 1, 2)
x = np.linspace(0, 10, 100)
y = x ** 2
ax3.plot(x, y)
ax3.set_title('Quadratic Function')
figtext_x = 0.5  
figtext_y = 0.02  
fig.text(figtext_x, figtext_y, 'Figure Text', fontsize=12, ha='center')

plt.tight_layout()

plt.savefig('my_figure.png', dpi=300, bbox_inches='tight')

plt.show()

plt.close(fig)
