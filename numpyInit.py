import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

# x = np.arange(0, 6, 0.1)
# y = np.sin(x)
#
# y2 = np.cos(x)

# plt.plot(x, y, label="sin")
# plt.plot(x, y2, linestyle="--", label="cos")
# plt.xlabel("x")
# plt.ylabel("y")
# plt.title("sin&cos")
# plt.legend()
# plt.show()

img = imread('E:/networkS/123.png')
plt.imshow(img)
plt.show()
