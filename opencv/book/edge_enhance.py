#!/usr/bin/env python3

"""Edge enhancement.
"""

import cv2
import numpy as np

img = cv2.imread("images/car.jpg")
img = cv2.resize(img, None, fx=0.25, fy=0.25, interpolation=cv2.INTER_AREA)
cv2.imshow("Original", img)
cv2.waitKey()

# Generate the kernels
kernel_sharpen_1 = np.array([[-1, -1, -1],
                             [-1, 9, -1],
                             [-1, -1, -1]])
kernel_sharpen_2 = np.array([[1, 1, 1],
                             [1, -7, 1],
                             [1, 1, 1]])
kernel_sharpen_3 = np.array([[-1, -1, -1, -1, -1],
                             [-1, 2, 2, 2, -1],
                             [-1, 2, 8, 2, -1],
                             [-1, 2, 2, 2, -1],
                             [-1, -1, -1, -1, -1]]) / 8.0

# Apply the kernels
output_1 = cv2.filter2D(img, -1, kernel_sharpen_1)
output_2 = cv2.filter2D(img, -1, kernel_sharpen_2)
output_3 = cv2.filter2D(img, -1, kernel_sharpen_3)
cv2.imshow("Sharpening", output_1)
cv2.waitKey()
cv2.imshow("Excessive sharpening", output_2)
cv2.waitKey()
cv2.imshow("Edge enhancement", output_3)
cv2.waitKey()
