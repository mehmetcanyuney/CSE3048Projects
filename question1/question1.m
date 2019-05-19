laplacian_kernel = fspecial("laplacian", 0.5);
gaussian_kernel = fspecial("gaussian", 5, 5);
sobel_kernel = fspecial("sobel");
motion_kernel = fspecial("motion", 40, 135);

image = imread('cameraman.tif');

imwrite(convolution(image, laplacian_kernel, 0), 'zero-lablacian.png')
imwrite(convolution(image, gaussian_kernel, 0), 'zero-gaussian.png')
imwrite(convolution(image, sobel_kernel, 0), 'zero-sobel.png')
imwrite(convolution(image, motion_kernel, 0), 'zero-motion.png')

imwrite(convolution(image, laplacian_kernel, 1), 'border-lablacian.png')
imwrite(convolution(image, gaussian_kernel, 1), 'border-gaussian.png')
imwrite(convolution(image, sobel_kernel, 1), 'border-sobel.png')
imwrite(convolution(image, motion_kernel, 1), 'border-motion.png')