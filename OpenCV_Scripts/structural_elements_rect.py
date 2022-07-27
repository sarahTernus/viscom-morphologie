import numpy as np
import cv2 as cv


def structuring_elements_rect():
    # Rectangular Kernel
    rect_kernel = cv.getStructuringElement(cv.MORPH_RECT, (20, 20))
    rect_small_vert = cv.getStructuringElement(cv.MORPH_RECT, (5, 20))
    rect_small_hor = cv.getStructuringElement(cv.MORPH_RECT, (20, 5))

    # Reading the input image
    img = cv.imread('../images/Beispielbild3_210x210.jpg', 0)
    if img is None:
        print('Could not open or find the erosion image: ')
        exit(0)

    # Erosion and Dilation functions
    img_erosion_rect = cv.erode(img, rect_kernel, iterations=1)
    img_erosion_rect_small_vert = cv.erode(img, rect_small_vert, iterations=1)
    img_erosion_rect_small_hor = cv.erode(img, rect_small_hor, iterations=1)

    img_dilation_rect = cv.dilate(img, rect_kernel, iterations=1)
    img_dilation_rect_small_vert = cv.dilate(img, rect_small_vert, iterations=1)
    img_dilation_rect_small_hor = cv.dilate(img, rect_small_hor, iterations=1)

    # Save result images
    cv.imshow('erosion_square', img_erosion_rect)
    cv.imshow('erosion_rect_vertical', img_erosion_rect_small_vert)
    cv.imshow('erosion_rect_horizontal', img_erosion_rect_small_hor)
    cv.waitKey(0)

    cv.imshow('dilation_square', img_dilation_rect)
    cv.imshow('dilation__rect_vertical', img_dilation_rect_small_vert)
    cv.imshow('dilation_rect_horizontal', img_dilation_rect_small_hor)
    cv.waitKey(0)


if __name__ == '__main__':
    structuring_elements_rect()

