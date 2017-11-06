#!/usr/bin/env python3

"""Detect a face.
"""

import cv2

img = cv2.imread("images/seimar_family.jpg")

img = cv2.resize(img, None, fx=0.25, fy=0.25,
                 interpolation=cv2.INTER_AREA)
result_img = img.copy()

face_cascade = cv2.CascadeClassifier("./cascade_files/haarcascade_"
                                     "frontalface_alt.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x, y, w, h) in face_rects:
    sub_face = img[y:y+h, x:x+w]
    sub_face = cv2.GaussianBlur(sub_face, (23, 23), 30)
    result_img[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face

cv2.imshow("Face detector", result_img)

c = cv2.waitKey()
