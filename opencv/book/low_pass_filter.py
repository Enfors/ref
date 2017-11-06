#!/usr/bin/env python3

"""Show parallellogram-like image using affine transformation.
"""

import cv2
import numpy as np

img = cv2.imread("images/link.jpg")

img = cv2.resize(img, None, fx=0.25, fy=0.25,
                 interpolation=cv2.INTER_AREA)

rows, cols = img.shape[:2]

kernel_identity = np.array([[0, 0, 0],
                            [0, 1, 0],
                            [0, 0, 0]])

kernel_3x3 = np.ones((3, 3), np.float32) / 9.0
kernel_5x5 = np.ones((5, 5), np.float32) / 25.0
kernel_9x9 = np.ones((9, 9), np.float32) / 81.0

kernel_5x1 = np.array([[0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [1, 1, 1, 1, 1],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0]]) / 5.0

cv2.imshow("Original", img)
cv2.waitKey()

output = cv2.filter2D(img, -1, kernel_identity)
cv2.imshow("Identity filter", output)
cv2.waitKey()

output = cv2.filter2D(img, -1, kernel_3x3)
cv2.imshow("3x3 filter", output)
cv2.waitKey()

output = cv2.filter2D(img, -1, kernel_5x5)
cv2.imshow("5x5 filter", output)
cv2.waitKey()

output = cv2.filter2D(img, -1, kernel_9x9)
cv2.imshow("9x9 filter", output)
cv2.waitKey()

output = cv2.filter2D(img, -1, kernel_5x1)
cv2.imshow("5x1 filter", output)
cv2.waitKey()

