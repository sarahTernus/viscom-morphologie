import numpy as np
import cv2 as cv


def hats():

    # Reading the input image
    img_top = cv.imread('images/top-hat.png', 0)
    img_black = cv.imread('images/black-hat.png', 0)
    img_selfdual = cv.imread('images/self-dual.png', 0)

    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((5, 5), np.uint8)
    # kernel2 = np.ones((2, 2), np.uint8)

    # The first parameter is the original image,
    top_hat = cv.morphologyEx(img_top, cv.MORPH_TOPHAT, kernel)
    black_hat = cv.morphologyEx(img_black, cv.MORPH_BLACKHAT, kernel)
    selfdual_hat = cv.morphologyEx(img_selfdual, cv.MORPH_BLACKHAT, kernel) + cv.morphologyEx(img_selfdual, cv.MORPH_TOPHAT, kernel)
    # selfdual_hat2 = (cv.morphologyEx(img_selfdual, cv.MORPH_CLOSE, kernel) - cv.morphologyEx(img_selfdual, cv.MORPH_OPEN, kernel))

    cv.imwrite('images/top-hat-result.png', top_hat)
    cv.imwrite('images/black-hat-result.png', black_hat)
    cv.imwrite('images/selfdual-hat-result.png', selfdual_hat)

    cv.waitKey(0)


if __name__ == '__main__':
    hats()
