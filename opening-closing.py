import numpy as np
import cv2 as cv


def opening_closing():

    # Reading the input image
    img_opening = cv.imread('images/opening.png', 0)
    img_closing = cv.imread('images/closing.png', 0)
    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((5, 5), np.uint8)

    # The first parameter is the original image,
    # kernel is the matrix with which image is
    # convolved and third parameter is the number
    # of iterations, which will determine how much
    # you want to erode/dilate a given image.
    opening = cv.morphologyEx(img_opening, cv.MORPH_OPEN, kernel)
    closing = cv.morphologyEx(img_closing, cv.MORPH_CLOSE, kernel)

    cv.imwrite('images/opening-result.png', opening)
    cv.imwrite('images/closing-result.png', closing)

    cv.waitKey(0)


if __name__ == '__main__':
    opening_closing()
