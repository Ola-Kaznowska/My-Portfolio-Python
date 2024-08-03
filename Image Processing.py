import cv2
import numpy as np
import math

def flip_image(img):
    new_img = []
    for row in range(img.shape[0]):
        new_row = []
        for column in range(img.shape[1]):
            new_row.append(img[row][-column-1])
        new_img.append(new_row)
    return np.array(new_img)

def filter(filter_array, img):
    new_img = img.copy()
    for row in range(1, img.shape[0] - 1):
        for column in range(1, img.shape[1] - 1):
            new_pixel = [0, 0, 0]
            for color in range(3):
                new_pixel[color] += img[row - 1][column - 1][color] * filter_array[0][0]
                new_pixel[color] += img[row][column - 1][color] * filter_array[1][0]
                new_pixel[color] += img[row + 1][column - 1][color] * filter_array[2][0]

                new_pixel[color] += img[row - 1][column][color] * filter_array[0][1]
                new_pixel[color] += img[row][column][color] * filter_array[1][1]
                new_pixel[color] += img[row + 1][column][color] * filter_array[2][1]

                new_pixel[color] += img[row - 1][column + 1][color] * filter_array[0][2]
                new_pixel[color] += img[row][column + 1][color] * filter_array[1][2]
                new_pixel[color] += img[row + 1][column + 1][color] * filter_array[2][2]

                new_pixel[color] = int(new_pixel[color])
                new_pixel[color] = max(0, new_pixel[color])
                new_pixel[color] = min(255, new_pixel[color])
            new_img[row][column] = new_pixel
    return np.array(new_img)

filename = "test.jpeg"

# img = cv2.imread(filename)
# cv2.imshow("Obraz bez modyfikacji", img)
# cv2.waitKey(0)

# img = cv2.imread(filename)
# img = flip_image(img)
# cv2.imshow("Lustrzane odbicie", img)
# cv2.imwrite(filename + "-flip", img)
# cv2.waitKey(0)

img = cv2.imread(filename)

# Sobel X
# img = filter([
#     [1, 0, -1],
#     [2, 0, -2],
#     [1, 0, -1]
#     ], img)

# Sobel Y
# img = filter([
#     [1, 2, 1],
#     [0, 0, 0],
#     [-1, -2, -1]
#     ], img)

# Emboss filter
# img = filter([
#     [-2, -1,  0],
#     [-1,  1,  1],
#     [ 0,  1,  2]
# ], img)

# Outline detector
# img = filter([
#     [-1, -1, -1],
#     [-1,  8, -1],
#     [-1, -1, -1]
# ], img)


# Gaussian blur
# img = filter([
#     [1/16, 2/16, 1/16],
#     [2/16, 4/16, 2/16],
#     [1/16, 2/16, 1/16]
# ], img)


# Sharpening filter
img = filter([
    [ 0, -1,  0],
    [-1,  5, -1],
    [ 0, -1,  0]
], img)


cv2.imshow("Filtr konwolucyjny - sobel", img)
cv2.imwrite("sharpening-" + filename, img)
cv2.waitKey(0)