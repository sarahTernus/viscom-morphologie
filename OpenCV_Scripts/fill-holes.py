import numpy as np
import cv2 as cv


def erosion_dilation():

    # Reading the input image
    img = cv.imread('../images/Erosion_Dilation/viscom.png', 0)
    if img is None:
        print('Could not open or find the image: ')
        exit(0)

    # Structural element
    kernel1 = np.ones((6, 1), np.uint8)

    # Erosion and Dilation functions
    img_dilation = cv.dilate(img, kernel1, iterations=1)

    # Save result images
    cv.imwrite('../images/results/dilation_viscom.png', img_dilation)


if __name__ == '__main__':
    erosion_dilation()

