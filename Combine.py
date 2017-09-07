import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.set_title("Average colour v/s Dominant colour")
img = mpimg.imread('Result.png')
ax1.imshow(img, aspect='auto')
# ax1.axis('off')


ax2 = fig.add_subplot(2,1,2)
img = mpimg.imread('ResultMode.png')
ax2.imshow(img, aspect='auto')
ax2.axis('off')
plt.tight_layout()
plt.show()