# -*- coding: utf-8 -*-
"""
Created on Tue May 28 16:14:30 2019

@author: T.Matsui
"""

import serial
import sys
import time
import csv


def SerialRead(PORT_Number, BitRate=115200):
    try:
        with serial.Serial(PORT_Number, BitRate, timeout = 0.1) as ser:
            while True:
                c = ser.readline()
                c = str(c, 'utf-8')
                print(c)

    except KeyboardInterrupt:
        print("Program Finished\n")
        sys.exit(0)


def SerialPrint(SerialData):
    while True:
        data = SerialData.readline()
        data = str(data, 'utf-8').replace("\r\n", "")
        data = data.split(",")
        # print(data)

        return data


def CheckSerialSend(PORT_Number, BitRate=115200):
    try:
        with serial.Serial(PORT_Number, BitRate, timeout = 0.1) as ser:
            print("Please input any key.")
            while True:
                # "Key入力受付"
                flag = bytes(input(), 'utf-8')

                # "a"入力時にプログラム終了
                if (flag == bytes('a', 'utf-8')):
                    break
                elif (flag == bytes('c', 'utf-8')):
                    ser.close()
                    print("Port closed.")
                    break

                elif (flag == bytes('s', 'utf-8')):
                    T1 = time.time()
                    ser.write(flag)
                    SerialPrint(ser)
                    T2 = time.time()
                    elapsed_time = T2-T1
                    print("処理時間={0:3f}[ms]".format(elapsed_time*1000))
                    break

    except KeyboardInterrupt:
        ser.close()
        print("Program Finished\n")
        sys.exit(0)


def SaveSerialSend(PORT_Number, BitRate=115200):
    try:
        with serial.Serial(PORT_Number, BitRate, timeout = 0.1) as ser:
            print("Please input any key.")
            while True:
                # "Key入力受付"
                flag = bytes(input(), 'utf-8')

                # "a"入力時にプログラム終了
                if (flag == bytes('a', 'utf-8')):
                    break
                # ポートクローズ
                elif (flag == bytes('c', 'utf-8')):
                    ser.close()
                    print("Port closed.")
                    break
                # シリアル読み取り
                elif (flag == bytes('s', 'utf-8')):
                    Header = ["Time","qd", "Degree", "tau", "rl",
                              "output"]
                    with open('EncorderData.csv', "w",  newline='') as f:
                        writer = csv.writer(f)
                        writer.writerow(Header)
                        ser.write(flag)
                        start_time = time.time()
                        now_time = 0
                        while True:
                            time.sleep(0.003)
                            now_time = time.time() - start_time
                            data = SerialPrint(ser)
                            writedata = [now_time]
                            writedata.extend(data)
                            writer.writerow(writedata)

    except KeyboardInterrupt:
        ser.close()
        print("Program Finished\n")
        sys.exit(0)


def SerialSend(PORT_Number, BitRate=115200):
    try:
        with serial.Serial(PORT_Number, BitRate, timeout = 0.1) as ser:
            print("Please input any key.")
            while True:
                # "Key入力受付"
                flag = bytes(input(), 'utf-8')

                # "a"入力時にプログラム終了
                if (flag == bytes('a', 'utf-8')):
                    break
                elif (flag == bytes('c', 'utf-8')):
                    ser.close()
                    print("Port closed.")
                    break

                elif (flag == bytes('s', 'utf-8')):
                    ser.write(flag)
                    SerialPrint(ser)
                    break

    except KeyboardInterrupt:
        ser.close()
        print("Program Finished\n")
        sys.exit(0)


if __name__ == '__main__':
    PORT = "COM13"
    BITRATE = 128000
    # SerialRead(PORT, BITRATE)
    CheckSerialSend(PORT, BITRATE)
    # SerialSend(PORT, BITRATE)
    # SaveSerialSend(PORT, BITRATE)
