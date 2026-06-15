import matplotlib.pyplot as plt
import numpy as np

# Create a sample 2D array (image data)
image_data = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

# Display the image using imshow
plt.imshow(image_data, cmap='viridis', interpolation='nearest', origin='upper')

# Add a color bar to the plot
plt.colorbar()

# Set axis labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sample Image')

# Show the plot
plt.show()
