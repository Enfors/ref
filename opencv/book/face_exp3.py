#!/usr/bin/env python3

"""Detect a face.
"""

import cv2

face_cascade = cv2.CascadeClassifier("./cascade_files/haarcascade_"
                                     "frontalface_alt.xml")

cap = cv2.VideoCapture(0)
scaling_factor = 1

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor,
                       interpolation=cv2.INTER_AREA)
    result_img = frame.copy()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_rects = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in face_rects:
        sub_face = frame[y:y+h, x:x+w]
        sub_face = cv2.GaussianBlur(sub_face, (23, 23), 30)
        result_img[y:y+sub_face.shape[0], x:x+sub_face.shape[1]] = sub_face

    cv2.imshow("Face detector", result_img)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
