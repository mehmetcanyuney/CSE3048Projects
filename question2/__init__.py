import numpy as np
from os.path import join
from matplotlib.image import imread, imsave
import matplotlib.pyplot as plt
from PIL import Image
from math import pow, sqrt
from __util__ import initFilters, createAverageTemplate


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

    print("Similarity => ", result)
    return result


def rgb2gray(rgb):
    temp = np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])
    for i in range(len(temp)):
        for j in range(len(temp[0])):
            temp[i][j] = int(temp[i][j])
    return temp


# initialize the filters -> transform the image to grayscale and resize
initFilters()
# creates the average template by taking average of given 4 train image
createAverageTemplate()

for i in range(2,6,1):
    input_path = "input" + str(i) + ".jpg"
    output_path = input_path.replace('input', 'output')
    print(input_path)

    image = imread(input_path)
    image = rgb2gray(image)
    train1 = imread('train1.png')
    train2 = imread('train2.png')
    train3 = imread('train3.png')
    train4 = imread('train4.png')
    avg_train = imread('avg_train.jpg')

    mt = MT(avg_train)
    const_denomitator = constCalc(avg_train, mt)

    pixel_jump = 50
    similarities = []
    for i in range(0, (len(image) - len(avg_train)), pixel_jump):
        for j in range(0, (len(image[0]) - len(avg_train[0])), pixel_jump):
            similarities.append([i, j, A(i, j, avg_train, image, mt, const_denomitator)])

    best = -1
    fx = None
    fy = None
    for i in similarities:
        if i[2] > best:
            best = i[2]
            fx = i[0]
            fy = i[1]

    print(fx, fy)

    image = np.array(image)

    recty = 100
    rectx = 120

    for i in range(recty + 1):
        image[fx][fy + i] = 0
        image[fx + rectx][fy + i] = 0
    for j in range(rectx + 1):
        image[fx + j][fy] = 0
        image[fx + j][fy + recty] = 0

    imsave(output_path, image, cmap='gray', vmin=0, vmax=256)
