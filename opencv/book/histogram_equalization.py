#!/usr/bin/env python3

"""Histogram equalization - making a dark image brighter.
"""

import cv2
import numpy as np

img = cv2.imread("images/dark_fox.jpg")
img = cv2.resize(img, None, fx=0.25, fy=0.25,
                 interpolation=cv2.INTER_AREA)

# Convert to suitable color space for changing brightness
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# Equalize the histogram of the Y channel
img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

# Convert the YUV image back to RGB format
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

cv2.imshow("Original", img)
cv2.waitKey()
cv2.imshow("Histogram equalized", img_output)
cv2.waitKey()
