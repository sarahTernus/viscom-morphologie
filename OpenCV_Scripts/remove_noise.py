import numpy as np
import cv2 as cv
import random


def add_noise(image):
    row, col = image.shape

    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        image[y_coord][x_coord] = 255

    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        image[y_coord][x_coord] = 0

    return image


def salt_pepper_noise_removal(image):

    kernel = np.ones((2, 2), np.uint8)

    opening = cv.morphologyEx(image, cv.MORPH_OPEN, kernel)
    closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)

    return closing


if __name__ == '__main__':
    img = cv.imread('../images/erau.jpeg', cv.IMREAD_GRAYSCALE)
    salt_and_pepper_erau = add_noise(img)
    cv.imwrite('../images/results/salt-pepper-erau.jpg', salt_and_pepper_erau)

    cv.imwrite('../images/results/removed-noise-erau.jpg', salt_pepper_noise_removal(salt_and_pepper_erau))
