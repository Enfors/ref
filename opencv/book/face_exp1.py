#!/usr/bin/env python3

"""Detect a face.
"""

import cv2

img = cv2.imread("images/seimar_family.jpg")

img = cv2.resize(img, None, fx=0.25, fy=0.25,
                 interpolation=cv2.INTER_AREA)

face_cascade = cv2.CascadeClassifier("./cascade_files/haarcascade_"
                                     "frontalface_alt.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in face_rects:
    cv2.rectangle(img, (x, y),
                  (x+w, y+h), (0, 255, 0), 3)

cv2.imshow("Face detector", img)

c = cv2.waitKey()
