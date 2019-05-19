import numpy as np
from os.path import join
from matplotlib.image import imread
import matplotlib.pyplot as plt

# Filters obtained from matlab
# Laplacian Kernel
laplacian_kernel = ([[0.33333, 0.33333, 0.33333],
                    [0.33333, -2.66667, 0.33333],
                    [0.33333, 0.33333, 0.33333]])
# Gaussian Kernel
gaussian_kernel = ([[0.036883, 0.039164, 0.039955, 0.039164, 0.036883],
                    [0.039164, 0.041586, 0.042426, 0.041586, 0.039164],
                    [0.039955, 0.042426, 0.043283, 0.042426, 0.039955],
                    [0.039164, 0.041586, 0.042426, 0.041586, 0.039164],
                    [0.036883, 0.039164, 0.039955, 0.039164, 0.036883]])
# Sobel Kernel
sobel_kernel = ([[1, 2, 1],
                 [0, 0, 0],
                 [-1, -2, -1]])
# Motion kernel
motion_kernel = ([[]])



def convolution(image, kernel, padding="zero"):
    kernel_rowsize = int(len(kernel))
    kernel_colsize = int(len(kernel[0]))

    image_rowsize = int(len(image))
    image_colsize = int(len(image[0]))

    conv_result = [[0 for i in range(image_rowsize)] for j in range(image_colsize)]

    for row in range(image_rowsize):
        for col in range(image_colsize):
            conv_sum = 0;
            for inner_row in range(kernel_rowsize):
                for inner_col in range(kernel_colsize):
                    loc_col = col + (inner_col - 1)
                    loc_row = row + (inner_row - 1)

                    if ((loc_col >= 0) and (loc_col < image_colsize)
                            and (loc_row >= 0) and (loc_row < image_rowsize)):
                        conv_sum = conv_sum + (image[loc_row][loc_col] * kernel[inner_row][inner_col])
                    # border padding
                    print(loc_col, loc_row)
                    if(padding == "border"):
                        if loc_col < 0:
                            if loc_row < 0:
                                conv_sum = conv_sum + (image[0][0] * kernel[inner_row][inner_col])
                            elif loc_row >= image_rowsize:
                                conv_sum = conv_sum + (image[image_rowsize - 1][0] * kernel[inner_row][inner_col])
                            else:
                                conv_sum = conv_sum + (image[loc_row][0] * kernel[inner_row][inner_col])
                        elif (loc_col >= 0) and (loc_col < image_colsize):
                            if loc_row < 0:
                                conv_sum = conv_sum + (image[0][loc_col] * kernel[inner_row][inner_col])
                            elif loc_row >= image_rowsize:
                                conv_sum = conv_sum + (image[image_rowsize - 1][loc_col] * kernel[inner_row][inner_col])
                        elif loc_col >= image_colsize:
                            if loc_row < 0:
                                conv_sum = conv_sum + (image[0][image_colsize - 1] * kernel[inner_row][inner_col])
                            elif loc_row >= image_rowsize:
                                conv_sum = conv_sum + (image[image_rowsize - 1][image_colsize - 1] * kernel[inner_row][inner_col])
                            else:
                                conv_sum = conv_sum + (image[loc_row][image_colsize - 1] * kernel[inner_row][inner_col])

            if conv_sum < 0:
                conv_sum = 0
            elif conv_sum > 256:
                conv_sum = 256

            conv_result[row][col] = conv_sum

    return conv_result



# image = imread('cameraman.tif')
#
# print(image[0])
# print(len(image[0]))
# print(len(image))
#
# plt.imshow(image, cmap='gray', vmin=0, vmax=256)
# plt.show()
