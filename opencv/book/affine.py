#!/usr/bin/env python3

"""Show parallellogram-like image using affine transformation.
"""

import cv2
import numpy as np

img = cv2.imread("images/input.jpg")

img = cv2.resize(img, None, fx=0.8, fy=0.8,
                 interpolation=cv2.INTER_AREA)

rows, cols = img.shape[:2]

src_points = np.float32([[0, 0], [cols-1, 0], [0, rows - 1]])
dst_points = np.float32([[0, 0],
                         [int(0.8*(cols - 1)), 0],
                         [int(0.2*(cols - 1)), rows - 1]])

affine_matrix = cv2.getAffineTransform(src_points, dst_points)
img_output = cv2.warpAffine(img, affine_matrix, (cols, rows))

cv2.imshow("Input", img)
cv2.waitKey()
cv2.imshow("Output", img_output)
cv2.waitKey()
