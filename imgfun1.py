#Write a program to show the use of imread,imsave,savefig functions
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
image = mpimg.imread('example.png')
fig, ax = plt.subplots()
ax.imshow(image)
ax.set_title('Example Image')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.colorbar(ax.imshow(image), ax=ax, orientation='vertical')
plt.savefig('output_image.png', dpi=300, bbox_inches='tight')
plt.show()
