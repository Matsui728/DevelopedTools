# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 14:58:52 2018

@author: kawalab
"""

import numpy as np
import cv2
from tqdm import tqdm


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('face1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, h, w) in tqdm(faces):
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)

    for (ex, ey, ew, eh) in tqdm(eyes):
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
        cv2.imshow("img", img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

print("Task is compleated!")