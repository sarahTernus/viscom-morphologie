import numpy as np
import cv2 as cv


def structuring_elements():
    # Rectangular Kernel
    rect_kernel = cv.getStructuringElement(cv.MORPH_RECT, (15, 15))

    # Elliptical Kernel
    ellipse_kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (15, 15))
    print(ellipse_kernel)

    # Cross-shaped Kernel
    cross_kernel = cv.getStructuringElement(cv.MORPH_CROSS, (15, 15))
    print(cross_kernel)

    # Reading the input image
    img = cv.imread('../images/beispielbild3.png', 0)
    if img is None:
        print('Could not open or find the erosion image: ')
        exit(0)

    # Erosion and Dilation functions
    img_erosion_rect = cv.erode(img, rect_kernel, iterations=1)
    img_erosion_ellipsis = cv.erode(img, ellipse_kernel, iterations=1)
    img_erosion_cross = cv.erode(img, cross_kernel, iterations=1)

    img_dilation_rect = cv.dilate(img, rect_kernel, iterations=1)
    img_dilation_ellipse = cv.dilate(img, ellipse_kernel, iterations=1)
    img_dilation_cross = cv.dilate(img, cross_kernel, iterations=1)

    # Save result images
    cv.imwrite('../images/SEresults/img_erosion_rectangle.png', img_erosion_rect)
    cv.imwrite('../images/SEresults/img_erosion_ellipsis.png', img_erosion_ellipsis)
    cv.imwrite('../images/SEresults/img_erosion_cross.png', img_erosion_cross)

    cv.imwrite('../images/SEresults/img_dilation_rectangle.png', img_dilation_rect)
    cv.imwrite('../images/SEresults/img_dilation_ellipse.png', img_dilation_ellipse)
    cv.imwrite('../images/SEresults/img_dilation_cross.png', img_dilation_cross)

    cv.waitKey(0)


if __name__ == '__main__':
    structuring_elements()

