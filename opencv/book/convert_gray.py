#!/usr/bin/env python3

"""Show how to load an image.
"""

import cv2

img = cv2.imread("images/input.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale image", gray_img)
cv2.waitKey()

yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
cv2.imshow("Converted", yuv_img)
cv2.waitKey()

cv2.imshow("Y channel", yuv_img[:, :, 0])
cv2.imshow("U channel", yuv_img[:, :, 1])
cv2.imshow("V channel", yuv_img[:, :, 2])
cv2.waitKey()

# Convert to HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV image", hsv_img)
