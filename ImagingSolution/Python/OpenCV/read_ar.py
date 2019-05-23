# -*- coding: utf-8 -*-
"""
Created on Wed Apr 25 18:07:24 2018

@author: kawalab
"""

import cv2

# ARマーカの情報を取得
aruco = cv2.aruco    # arucoライブラリ
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)


def arReader():
    cap1 = cv2.VideoCapture(0)       # キャプチャ開始
    cap2 = cv2.VideoCapture(1)
    while True:

        ret1, frame1 = cap1.read()     # ビデオキャプチャから画像を取得
        ret2, frame2 = cap2.read()

        Height1, Widrh1 = frame1.shape[:2]     # サイズを取得
        Height2, Widrh2 = frame2.shape[:2]     # サイズを取得

        img1 = cv2.resize(frame1, (int(Widrh1), int(Height1)))
        img2 = cv2.resize(frame2, (int(Widrh2), int(Height2)))


        # マーカを検出(関数2番目の引数がID値)
        corners, ids, rejectedImgPoints = aruco.detectMarkers(img1,
                                                              dictionary)

        # 検出したマーカに描画する
        aruco.drawDetectedMarkers(img1, corners, ids, (0, 255, 0))


        cv2.imshow('drawDetectedMarkers', img1)      # マーカが描画された画像を表示
        cv2.imshow('Example', img2)      # マーカが描画された画像を表示
        # print("ID is " + str(ids))

        if cv2.waitKey(33) >= 0:
            break

    cap1.release()        # ビデオキャプチャのメモリ解放
    cap2.release()        # ビデオキャプチャのメモリ解放
    cv2.destroyAllWindows()         # すべてのウィンドウを閉じる



if __name__ == '__main__':
    arReader()
