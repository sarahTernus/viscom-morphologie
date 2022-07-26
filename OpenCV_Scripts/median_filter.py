import numpy as np
import cv2 as cv


def median():

    # Reading the input image
    img = cv.imread('../images/salt-pepper-erau.jpg', 0)

    # Median Filter Function
    median_filter = cv.medianBlur(img, 3)

    # Save result image
    cv.imwrite('../images/results/median-erau.jpg', median_filter)
    cv.waitKey(0)


if __name__ == '__main__':
    median()
