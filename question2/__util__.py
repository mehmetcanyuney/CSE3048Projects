import numpy as np
from os.path import join
from matplotlib.image import imread, imsave
import matplotlib.pyplot as plt
from PIL import Image
import PIL
from math import pow, sqrt


def initFilters():
    train1 = Image.open('train1-rgb.png').convert('L')
    train1 = train1.resize((101,126), PIL.Image.ANTIALIAS)
    train1.save('train1.png')

    train2 = Image.open('train2-rgb.png').convert('L')
    train2 = train2.resize((101,126), PIL.Image.ANTIALIAS)
    train2.save('train2.png')

    train3 = Image.open('train3-rgb.png').convert('L')
    train3 = train3.resize((101,126), PIL.Image.ANTIALIAS)
    train3.save('train3.png')

    train4 = Image.open('train4-rgb.png').convert('L')
    train4 = train4.resize((101,126), PIL.Image.ANTIALIAS)
    train4.save('train4.png')

def createAverageTemplate():
    train1 = Image.open('train1.png').convert('L')
    train2 = Image.open('train2.png').convert('L')
    train3 = Image.open('train3.png').convert('L')
    train4 = Image.open('train4.png').convert('L')

    i, j = train1.size

    train1 = train1.load()
    train2 = train2.load()
    train3 = train3.load()
    train4 = train4.load()

    avg_template = Image.new('L', (i, j))

    for k in range(i):
        for l in range(j):
            avg_template.putpixel((k, l), int((train1[k,l] + train2[k,l] + train3[k,l] + train4[k,l]) / 4))

    avg_template.save("avg_train.jpg")
