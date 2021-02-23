from pathlib import Path
import numpy
import skimage.io
import skimage.color
from matplotlib import pyplot
from scipy.signal import convolve2d


def edge_detection():

    sigma_value = 2
    threshold = 30

    image_path = Path('edge.jpg')

    image = skimage.io.imread(image_path.as_posix())
    height, width = image.shape

    gauss_kernel_size = 5
    gaussian_blur = numpy.zeros((gauss_kernel_size, gauss_kernel_size), dtype=float)
    x = int(gauss_kernel_size / 2)
    y = int(gauss_kernel_size / 2)

    for m in range(-x, x + 1):
        for n in range(-y, y + 1):
            x1 = 2 * numpy.pi * (sigma_value ** 2)
            x2 = numpy.exp(-(m ** 2 + n ** 2) / (2 * sigma_value ** 2))
            gaussian_blur[m + x, n + y] = x2 / x1

    image_smooth = convolve2d(image, gaussian_blur, boundary='symm', mode='same')

    sobel_x = numpy.array([[-1, 0, 1],
                           [-2, 0, 2],
                           [-1, 0, 1]])

    sobel_y = numpy.array([[-1, -2, -1],
                           [0, 0, 0],
                           [1, 2, 1]])

    image_x = convolve2d(image_smooth, sobel_x)
    image_y = convolve2d(image_smooth, sobel_y)

    image_magnitude = numpy.zeros(image.shape, dtype=float)
    for i in range(height):
        for j in range(width):
            image_magnitude[i, j] = numpy.sqrt(image_x[i, j]**2 + image_y[i, j]**2)

    binary_image = numpy.zeros(image.shape, dtype=int)

    for i in range(height):
        for j in range(width):
            if image_magnitude[i, j] >= threshold:
                binary_image[i, j] = 1
            else:
                binary_image[i, j] = 0

    pyplot.subplot(231)
    pyplot.imshow(image, cmap='gray')
    pyplot.title(f'Original Image')
    pyplot.subplot(232)
    pyplot.imshow(image_smooth, cmap='gray')
    pyplot.title(f'Image using Gaussian filter sigma ={sigma_value} ')
    pyplot.subplot(233)
    pyplot.imshow(image_x, cmap='gray')
    pyplot.title(f'Image Gradient x')
    pyplot.subplot(234)
    pyplot.imshow(image_y, cmap='gray')
    pyplot.title(f'Image Gradient y')
    pyplot.subplot(235)
    pyplot.imshow(image_magnitude, cmap='gray')
    pyplot.title(f'Image Gradient Magnitude')
    pyplot.subplot(236)
    pyplot.imshow(binary_image, cmap='gray')
    pyplot.title(f'Binary Image using threshold T={threshold}')
    pyplot.show()

    return


def main():

    edge_detection()

    return


if __name__ == '__main__':
    main()
