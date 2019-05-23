# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 15:31:42 2018

@author: kawalab
"""
import cv2
img = cv2.imread("lena.jpg")

cv2.namedWindow("window")
cv2.imshow("window", img)
cv2.waitKey(0)
cv2.destroyAllWindows()