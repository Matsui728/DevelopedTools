# -*- coding: utf-8 -*-
"""
@author: T.Matsui
"""

import cv2
import math

# ARマーカの情報を取得
aruco = cv2.aruco    # arucoライブラリ
dictionary = aruco.getPredefinedDictionary(aruco.DICT_4X4_50)


def CenterPoint(CornerData):
    up_x = (CornerData[0][0] + CornerData[1][0]) / 2
    down_x = (CornerData[2][0] + CornerData[3][0]) / 2
    left_y = (CornerData[0][1] + CornerData[3][1]) / 2
    right_y = (CornerData[1][1] + CornerData[2][1]) / 2

    center_x = int((up_x + down_x)/2)
    center_y = int((left_y + right_y)/2)
    CenterPoint = [center_x, center_y]

    return CenterPoint


def GetCornerData(corners):
    # ARマーカの各コーナーの座標を取得(左上、右上、右下,左下)
    Cornertemp = []
    CornerData = []
    for i in range(4):
        Point = corners[0][0][i]
        Cornertemp.append(Point)
        for j in range(len(Cornertemp)):
            x = Cornertemp[j][0]
            y = Cornertemp[j][1]
            Temp = [x, y]
        CornerData.append(Temp)
    return CornerData


def SaveMousePoint(PointData):
    x = PointData[0]
    y = PointData[1]

    return x, y


def WriteMousePoint(img, xPoint, yPoint):
    cv2.circle(img, (xPoint, yPoint),
               5, (0, 0, 255), thickness=-1)


def CalculateTheta(Point1, Point2):
    theta = -math.degrees(math.atan2((Point2[1]-Point1[1]),
                                    (Point2[0]-Point1[0])))

    return theta


class MouseParam:
    def __init__(self, input_img_name):
        # マウス入力用のパラメータ
        self.mouseEvent = {"x": None, "y": None,
                           "event": None, "flags": None}

        # マウス入力の設定
        cv2.setMouseCallback(input_img_name, self.__CallBackFunc, None)

    # コールバック関数
    def __CallBackFunc(self, eventType, x, y, flags, userdata):

        self.mouseEvent["x"] = x
        self.mouseEvent["y"] = y
        self.mouseEvent["event"] = eventType
        self.mouseEvent["flags"] = flags

    # マウス入力用のパラメータを返すための関数
    def getData(self):
        return self.mouseEvent

    # マウスイベントを返す関数
    def getEvent(self):
        return self.mouseEvent["event"]

    # マウスフラグを返す関数
    def getFlags(self):
        return self.mouseEvent["flags"]

    # xの座標を返す関数
    def getX(self):
        return self.mouseEvent["x"]

    # yの座標を返す関数
    def getY(self):
        return self.mouseEvent["y"]

    # xとyの座標を返す関数
    def getPos(self):
        return (self.mouseEvent["x"], self.mouseEvent["y"])


def arReader():
    mousepoint_x, mousepoint_y = 0, 0
    MousePointData = [mousepoint_x, mousepoint_y]
    theta = 0
    cap1 = cv2.VideoCapture(0)

    WindowName = "Result"

    while True:

        ret1, frame1 = cap1.read()

        Height1, Widrh1 = frame1.shape[:2]

        img1 = cv2.resize(frame1, (int(Widrh1), int(Height1)))

        # マーカを検出(関数2番目の引数がID値)
        corners, ids, rejectedImgPoints = aruco.detectMarkers(img1,
                                                              dictionary)

        # aruco.drawDetectedMarkers(img1, corners, ids, (0, 255, 0))
        print("ID is " + str(ids))
        if (str(ids) != "None"):
            CornerData = GetCornerData(corners)
            Point = CenterPoint(CornerData)
            cv2.circle(img1, (Point[0], Point[1]),
                       5, (0, 255, 0), thickness=-1)

        else:
            CornerData = "NO DATA"
            print(CornerData)

        # cv2.imshow(WindowName, img1)
        mouseData = MouseParam(WindowName)

        if cv2.waitKey(20):
            # 左クリックがあったら表示
            if mouseData.getEvent() == cv2.EVENT_LBUTTONDOWN:
                mousepoint_x, mousepoint_y = (mouseData.getPos())
                MousePointData = [mousepoint_x, mousepoint_y]


            # 右クリックがあったら終了
            elif mouseData.getEvent() == cv2.EVENT_RBUTTONDOWN:
                break

        theta = CalculateTheta(MousePointData, Point)
        print("theta = {:.3f}".format(theta))
        WriteMousePoint(img1, mousepoint_x, mousepoint_y)
        cv2.imshow(WindowName, img1)

    # aruco.drawDetectedMarkers()
    cap1.release()        # ビデオキャプチャのメモリ解放
    cv2.destroyAllWindows()         # すべてのウィンドウを閉じる


if __name__ == '__main__':
    arReader()
