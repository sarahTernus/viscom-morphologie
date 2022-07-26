import numpy as np
import cv2 as cv


def erosion_dilation():

    # Reading the input image
    img_erosion = cv.imread('../images/Erosion_Dilation/erosion-example.png', 0)
    img_dilation = cv.imread('../images/Erosion_Dilation/dilation-example.png', 0)

    if img_erosion is None:
        print('Could not open or find the erosion image: ')
        exit(0)

    if img_dilation is None:
        print('Could not open or find the dilation image: ')
        exit(0)

    # Structural element
    kernel = np.ones((6, 6), np.uint8)

    # Erosion and Dilation functions
    img_erosion_result = cv.erode(img_erosion, kernel, iterations=1)
    img_dilation_result = cv.dilate(img_dilation, kernel, iterations=1)

    # Save result images
    cv.imwrite('../images/results/erosion-result.png', img_erosion_result)
    cv.imwrite('../images/results/dilation-result.png', img_dilation_result)

    cv.waitKey(0)


if __name__ == '__main__':
    erosion_dilation()

