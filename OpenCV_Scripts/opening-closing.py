import numpy as np
import cv2 as cv


def opening_closing():

    # Reading the input image
    img_opening = cv.imread('../images/Opening_Closing/oeffnung.png', 0)
    img_closing = cv.imread('../images/Opening_Closing/schliessung.png', 0)
    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((6, 6), np.uint8)

    # The first parameter is the original image,
    # kernel is the matrix with which image is
    # convolved and third parameter is the number
    # of iterations, which will determine how much
    # you want to erode/dilate a given image.
    opening = cv.morphologyEx(img_opening, cv.MORPH_OPEN, kernel)
    closing = cv.morphologyEx(img_closing, cv.MORPH_CLOSE, kernel)

    cv.imwrite('../images/results/oeffnung-result.png', opening)
    cv.imwrite('../images/results/schliessung-result.png', closing)


if __name__ == '__main__':
    opening_closing()
