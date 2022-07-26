import numpy as np
import cv2 as cv


def structuring_elements_rect():
    # Rectangular Kernel
    rect_kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    rect_small_vert = cv.getStructuringElement(cv.MORPH_RECT, (1, 3))
    rect_small_hor = cv.getStructuringElement(cv.MORPH_RECT, (3, 1))

    # Reading the input image
    img = cv.imread('../images/beispielbild.png', 0)
    if img is None:
        print('Could not open or find the erosion image: ')
        exit(0)

    # Erosion and Dilation functions
    img_erosion_rect = cv.erode(img, rect_kernel, iterations=1)
    img_erosion_rect_small_vert = cv.erode(img, rect_small_vert, iterations=1)
    img_erosion_rect_small_hor = cv.erode(img, rect_small_hor, iterations=1)

    img_dilation_rect = cv.dilate(img, rect_kernel, iterations=1)
    img_dilation_rect_small_vert = cv.erode(img, rect_small_vert, iterations=1)
    img_dilation_rect_small_hor = cv.erode(img, rect_small_hor, iterations=1)

    # Save result images
    cv.imwrite('../images/SEresults/img_erosion_rect.png', img_erosion_rect)
    cv.imwrite('../images/SEresults/img_erosion_rect_small_vert.png', img_erosion_rect_small_vert)
    cv.imwrite('../images/SEresults/img_erosion_rect_small_hor.png', img_erosion_rect_small_hor)

    cv.imwrite('../images/SEresults/img_dilation_rect.png', img_dilation_rect)
    cv.imwrite('../images/SEresults/img_dilation_rect_small_vert.png', img_dilation_rect_small_vert)
    cv.imwrite('../images/SEresults/img_dilation_rect_small_hor.png', img_dilation_rect_small_hor)

    cv.waitKey(0)


if __name__ == '__main__':
    structuring_elements_rect()

