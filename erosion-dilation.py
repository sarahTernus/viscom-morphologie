import numpy as np
import cv2 as cv


def erosion_dilation():

    # Reading the input image
    img = cv.imread('images/example_T.png', 0)
    if img is None:
        print('Could not open or find the image: ')
        exit(0)

    # Structural element
    kernel = np.ones((10, 10), np.uint8)

    # Erosion and Dilation functions
    img_erosion = cv.erode(img, kernel, iterations=1)
    img_dilation = cv.dilate(img, kernel, iterations=1)

    # Save result images
    cv.imwrite('images/erosion_T.png', img_erosion)
    cv.imwrite('images/dilation_T.png', img_dilation)

    cv.waitKey(0)


if __name__ == '__main__':
    erosion_dilation()

