# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:52:57 2018

@author: kawalab
"""

import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

cv2.namedWindow('preview')
cv2.namedWindow("img")

while(True):
    ret1, img1 = cap.read()
    cv2.imshow('preview', img1)
    ret2, img2 = cap.read()

    gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    if ret1 == False:
        continue


    for (x,y,w,h) in faces:
        cv2.rectangle(img2,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img2[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)


        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            cv2.imshow('img', img2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
