import numpy as np
from os.path import join
from matplotlib.image import imread, imsave
import matplotlib.pyplot as plt
from PIL import Image
from math import pow, sqrt


image = imread('test.jpg')
image = np.array(image)
x = 30
y = 50

for i in range(88):
    image[x][y + i] = 0
    image[x + 120][y + i] = 0
for j in range(120):
    image[x + j][y] = 0
    image[x + j][y + 87] = 0

plt.imshow(image)
plt.show()
