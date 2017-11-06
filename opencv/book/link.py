#!/usr/bin/env python3

"""Show Link.
"""

import cv2
import numpy as np

img = cv2.imread("images/link.jpg")
img_scaled = cv2.resize(img, None, fx=0.27, fy=0.27,
                        interpolation=cv2.INTER_AREA)
cv2.imshow("Scaling - Linear Interpolation", img_scaled)
cv2.waitKey()

