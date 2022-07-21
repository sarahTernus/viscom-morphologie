import numpy as np
import cv2 as cv


def erosion_dilation():

    # Reading the input image
    img = cv.imread('images/beispielbild2.png', 0)
    if img is None:
        print('Could not open or find the image: ')
        exit(0)

    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((3, 3), np.uint8)

    # The first parameter is the original image,
    # kernel is the matrix with which image is
    # convolved and third parameter is the number
    # of iterations, which will determine how much
    # you want to erode/dilate a given image.
    img_erosion = cv.erode(img, kernel, iterations=1)
    img_dilation = cv.dilate(img, kernel, iterations=1)

    cv.imwrite('images/erosion.png', img_erosion)
    cv.imwrite('images/dilation.png', img_dilation)

    cv.waitKey(0)


if __name__ == '__main__':
    erosion_dilation()

