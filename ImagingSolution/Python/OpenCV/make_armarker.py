# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 18:07:22 2018

@author: kawalab
"""

import cv2

aruco = cv2.aruco
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)   # マーカーデータを取得


def arGenerator():
    for i in range(37):
        # ２番目の引数がマーカーのID値，　3番目の引数が画像の大きさ
        generator = aruco.drawMarker(dictionary, i, 200)
        num = i
        fileName = "{}.png".format(num)
        cv2.imwrite(fileName, generator)

    print("End tasks.")
if __name__ == '__main__':
    arGenerator()