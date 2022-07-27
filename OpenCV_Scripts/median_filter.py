
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


def median(image):
    # Median Filter Function
    median_filter = cv.medianBlur(img, 3)

    # Save result image
    cv.imwrite('../images/results/median-erau.jpg', median_filter)


if __name__ == '__main__':
    # reading input image and creating noise on image
    img = cv.imread('../images/erau.jpeg', cv.IMREAD_GRAYSCALE)
    salt_and_pepper_erau = add_noise(img)

    # call median function
    median(salt_and_pepper_erau)
