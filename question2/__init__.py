import numpy as np
from os.path import join
from matplotlib.image import imread, imsave
import matplotlib.pyplot as plt
from PIL import Image
from math import pow, sqrt

def MT(avg):
    p = len(avg)
    q = len(avg[0])

    result = 0
    for r in range(p):
        for s in range(q):
            result = result + avg[r][s]
    result = result / (p * q)

    return result

def MI(x, y, avg, image):
    p = len(avg)
    q = len(avg[0])

    result = 0
    for r in range(p):
        for s in range(q):
            result = result + image[x + r][y + s]
    result = result / (p * q)

    return result

def constCalc(avg, mt):
    p = len(avg)
    q = len(avg[0])

    result = 0
    for r in range(p):
        for s in range(q):
            temp = avg[r][s] - mt
            result = result + pow(temp, 2)
    result = sqrt(result)

    return result

def A(x,y, avg, image, mt, cons):
    p = len(avg)
    q = len(avg[0])

    temp = 0
    for r in range(p):
        for s in range(q):
            temp = temp + float((avg[r][s] - mt) * (image[x + r][y + s] - MI(x, y, avg, image)))
    proportion = temp

    temp = 0
    for r in range(p):
        for s in range(q):
            temp = temp + pow((image[x + r][y + s] - MI(x, y, avg, image)), 2)
    temp = sqrt(temp)

    denominator = cons * temp

    result = proportion / denominator
    print(result)
    return result

def rgb2gray(rgb):
    temp = np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            temp[i][j] = int(temp[i][j])
    return temp

image = imread('test.jpg')
image = rgb2gray(image)
train1 = imread('train1.png')
train1 = rgb2gray(train1)
train2 = imread('train2.png')
train2 = rgb2gray(train2)
train3 = imread('train3.png')
train3 = rgb2gray(train3)
train4 = imread('train4.png')
train4 = rgb2gray(train4)

### run once ###
# avg_train = [[0 for  i in range(len(train1[0]))] for j in range(len(train1))]
#
# for row in range(len(train1)):
#     for col in range(len(train1[0])):
#         sum = train1[row][col] + train2[row][col] + train3[row][col]
#         avg = int(sum / 3)
#         avg_train[row][col] = avg
# avg_train = np.array(avg_train)
#
# plt.imshow(avg_train, cmap='gray', vmin=0, vmax=256)
# plt.show()
#
# imsave('avg_train.jpg', avg_train, cmap='gray', vmin=0, vmax=256)

# avg_train = imread('avg_train.jpg')
#
# mt = MT(avg_train)
# const_denomitator = constCalc(avg_train, mt)
#
# similarities = []
# for i in range(0, (len(image) - len(avg_train)), 50):
#     for j in range(0, (len(image[0]) - len(avg_train[0])), 50):
#         similarities.append([i, j, A(i, j, avg_train, image, mt, const_denomitator)])
#
# best = -1
# fx = None
# fy = None
# for i in similarities:
#     if i[2] > best:
#         best = i[2]
#         fx = i[0]
#         fy = i[1]
#
# print(fx, fy)

fx = 0
fy = 150

image = np.array(image)

recty = 100
rectx = 120

for i in range(recty + 1):
    image[fx][fy + i] = 0
    image[fx + rectx][fy + i] = 0
for j in range(rectx + 1):
    image[fx + j][fy] = 0
    image[fx + j][fy + recty] = 0

plt.imshow(image, cmap='gray', vmin=0, vmax=256)
plt.show()
