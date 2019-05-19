import numpy as np
from os.path import join
from matplotlib.image import imread
import matplotlib.pyplot as plt

train1 = imread('train1.jpg')
train2 = imread('train2.jpg')
train3 = imread('train3.jpg')
train4 = imread('train4.jpg')

avg_train = [[0 for  i in range(len(train1[0]))] for j in range(len(train1))]

for row in range(len(train1)):
    for col in range(len(train1[0])):
        sum = train1[row][col] + train2[row][col] + train3[row][col] + train4[row][col]
        avg = int(sum / 4)
        avg_train[row][col] = avg

plt.imshow(avg_train, cmap='gray', vmin=0, vmax=256)
plt.show()
