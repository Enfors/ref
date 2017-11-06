#!/usr/bin/env python3

"""Show how to load an image.
"""

import cv2

img = cv2.imread("images/input.jpg")
cv2.imshow("Input image", img)
cv2.waitKey()
