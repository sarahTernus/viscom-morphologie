import numpy as np
import cv2 as cv


def hats():

    # Reading the input image
    img = cv.imread('images/gradient-example.jpg', 0)

    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((5, 5), np.uint8)

    beucher = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
    # oder
    beucher2 = cv.dilate(img, kernel, iterations=1) - cv.erode(img, kernel, iterations=1)

    internal = img - cv.erode(img, kernel, iterations=1)
    external = cv.dilate(img, kernel, iterations=1) - img


    cv.imwrite('images/beucher-result.png', beucher)
    cv.imwrite('images/beucher2-result.png', beucher2)
    cv.imwrite('images/internal-result.png', internal)
    cv.imwrite('images/external-hat-result.png', external)

    cv.waitKey(0)


if __name__ == '__main__':
    hats()
