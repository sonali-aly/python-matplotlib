import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# Load an image using matplotlib.image.imread
image = mpimg.imread('example.png')

# Create a figure and axis for displaying the image
fig, ax = plt.subplots()

# Display the image using imshow
ax.imshow(image)

# Customize the plot by adding labels, title, and colorbar
ax.set_title('Example Image')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.colorbar(ax.imshow(image), ax=ax, orientation='vertical')

# Show the plot
plt.show()
