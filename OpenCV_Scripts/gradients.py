import numpy as np
import cv2 as cv


def gradients():

    # Reading the input image
    img = cv.imread('../images/Gradients/gradient-example.jpg', 0)

    # Taking a matrix of size 5 as the kernel
    kernel = np.ones((5, 5), np.uint8)

    # Using 2 different versions to create morphological gradient
    beucher = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel)
    # oder
    beucher2 = cv.dilate(img, kernel, iterations=1) - cv.erode(img, kernel, iterations=1)

    # internal and external gradient
    internal = img - cv.erode(img, kernel, iterations=1)
    external = cv.dilate(img, kernel, iterations=1) - img

    cv.imwrite('../images/results/beucher-result.png', beucher)
    cv.imwrite('../images/results/beucher2-result.png', beucher2)
    cv.imwrite('../images/results/internal-result.png', internal)
    cv.imwrite('../images/results/external-result.png', external)



if __name__ == '__main__':
    gradients()
