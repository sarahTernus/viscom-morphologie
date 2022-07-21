import numpy as np
import cv2 as cv


def hats():

    # Reading the input image
    img = cv.imread('images/testimage-2.png', 0)

    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((2, 2), np.uint8)

    # The first parameter is the original image,
    # kernel is the matrix with which image is
    # convolved and third parameter is the number
    # of iterations, which will determine how much
    # you want to erode/dilate a given image.
    top_hat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
    black_hat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

    cv.imwrite('images/top-hat.png', top_hat)
    cv.imwrite('images/black-hat.png', black_hat)

    cv.waitKey(0)


if __name__ == '__main__':
    hats()
