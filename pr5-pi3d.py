import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Data to plot
labels = 'A', 'B', 'C', 'D'
sizes = [15, 30, 45, 10]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Calculate the angles for the wedge shapes
angles = [360 * size / sum(sizes) for size in sizes]

# Starting angle for the first wedge
start_angle = 0

# Plot the 3D-like pie chart
for label, size, color, angle in zip(labels, sizes, colors, angles):
    ax.bar3d(0, 0, 0, 1, 1, 1, color=color, shade=True, alpha=0.7)
    ax.text(1.5, 0, 0.5, label, ha='center', va='center', fontsize=12)
    ax.text(1.5, 0, 1.2, f'{size}%', ha='center', va='center', fontsize=10)
    ax.view_init(elev=20, azim=start_angle)
    start_angle += angle

# Set aspect ratio to be equal
ax.auto_scale_xyz([0, 2], [0, 2], [0, 2])

# Hide the axes
ax.grid(False)

# Show the chart
plt.show()
