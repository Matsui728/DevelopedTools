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



def SaveAngleData(PORT_Number, BitRate=115200):
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
                    print("Save Start!")
                    Header = ["Time","Degree"]
                    with open('MaqgneticEncoder.csv', "w",  newline='') as f:
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

                elif (flag == bytes('h', 'utf-8')):
                    ser.write(flag)
                    SerialPrint(ser)
                    break

                elif (flag ==  bytes('z', 'utf-8')):
                    ser.write(flag)
                    data = ser.readline()
                    data = str(data, 'utf-8')
                    print(data)

                elif (flag ==  bytes('e', 'utf-8')):
                    ser.write(flag)
                    while(1):
                        data = ser.readline()
                        data = str(data, 'utf-8')
                        print("\r"+data, end="")
                        sys.stdout.flush()

                elif (flag ==  bytes('s', 'utf-8')):
                    ser.write(flag)
                    while(1):
                        data = ser.readline()
                        data = str(data, 'utf-8')
                        print("\r"+data, end="")
                        sys.stdout.flush()




    except KeyboardInterrupt:
        ser.close()
        print("Program Finished\n")
        sys.exit(0)


def MotorControl(PORT_Number, BitRate=115200):
    try:
        with serial.Serial(PORT_Number, BitRate, timeout = 0.1) as ser:
            print("Please input any key.")
            ser.reset_output_buffer()
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

                elif (flag == bytes('h', 'utf-8')):
                    ser.write(flag)
                    SerialPrint(ser)
                    break

                elif (flag ==  bytes('z', 'utf-8')):
                    ser.write(flag)
                    data = ser.readline()
                    data = str(data, 'utf-8')
                    print(data)

                elif (flag ==  bytes('e', 'utf-8')):
                    ser.write(flag)
                    while(1):
                        data = ser.readline()
                        data = str(data, 'utf-8')
                        print("\r"+data, end="")
                        sys.stdout.flush()

                elif (flag ==  bytes('s', 'utf-8')):
                    ser.write(flag)
                    print("Save Start!")
                    Header = ["Time","Degree", "Degree2", "LInk_angle"]
                    Header2 = ["0", "0", "0", "0"]

                with open('Angle.csv', "w",  newline='') as f:
                   writer = csv.writer(f)
                   writer.writerow(Header)
                   writer.writerow(Header2)
                   ser.reset_input_buffer()
                   ser.reset_output_buffer()
                   while True:
                       data = SerialPrint(ser)
                       writedata = []
                       writedata.extend(data)
                       writer.writerow(writedata)

    except KeyboardInterrupt:
        ser.close()
        print("Program Finished\n")
        sys.exit(0)

def AntagonisticControl(PORT_Number1, PORT_Number2, BitRate=115200):
    try:
        with serial.Serial(PORT_Number1, BitRate, timeout = 0.1) as ser1:
            with serial.Serial(PORT_Number2, BitRate, timeout = 0.1) as ser2:
                print("Please input any key.")
                ser1.reset_output_buffer()
                ser2.reset_output_buffer()
                while True:
                    # "Key入力受付"
                    flag = bytes(input(), 'utf-8')

                    # "a"入力時にプログラム終了
                    if (flag == bytes('a', 'utf-8')):
                        break
                    elif (flag == bytes('c', 'utf-8')):
                        ser1.close()
                        ser2.close()
                        print("Port closed.")
                        break

                    elif (flag == bytes('h', 'utf-8')):
                        ser1.write(flag)
                        ser2.write(flag)
                        SerialPrint(ser1)
                        SerialPrint(ser2)
                        break

                    elif (flag ==  bytes('z', 'utf-8')):
                        ser1.write(flag)
                        ser2.write(flag)
                        data1 = ser1.readline()
                        data2 = ser2.readline()
                        data1 = str(data1, 'utf-8')
                        print(data1)
                        data2 = str(data2, 'utf-8')
                        print(data2)

                    elif (flag ==  bytes('e', 'utf-8')):
                        ser1.write(flag)
                        ser2.write(flag)
                        while(1):
                            data1 = ser1.readline()
                            data1 = str(data1, 'utf-8')
                            print("\r"+data1, end="")
                            data2 = ser2.readline()
                            data2 = str(data2, 'utf-8')
                            print("\r"+data2, end="")
                            sys.stdout.flush()

                    elif (flag ==  bytes('s', 'utf-8')):
                        ser1.write(bytes('s', 'utf-8'))
                        ser2.write(bytes('s', 'utf-8'))
                        print("Save Start!")
                        Header = ["Time", "Degree", "Degree2", "LInk_angle"]
                        Header2 = ["0", "0", "0", "0"]

                    with open('Angle1.csv', "w",  newline='') as f1:
                        with open('Angle2.csv', "w",  newline='') as f2:
                            # マイコン1書き込み
                            writer1 = csv.writer(f1)
                            writer1.writerow(Header)
                            writer1.writerow(Header2)
                            ser1.reset_input_buffer()
                            ser1.reset_output_buffer()

                            # マイコン2書き込み
                            writer2 = csv.writer(f2)
                            writer2.writerow(Header)
                            writer2.writerow(Header2)
                            ser2.reset_input_buffer()
                            ser2.reset_output_buffer()

                            while True:
                                data1 = SerialPrint(ser1)
                                writedata1 = []
                                writedata1.extend(data1)
                                writer1.writerow(writedata1)

                                data2 = SerialPrint(ser2)
                                writedata2 = []
                                writedata2.extend(data2)
                                writer2.writerow(writedata2)

    except KeyboardInterrupt:
        ser1.close()
        ser2.close()
        print("Program Finished\n")
        sys.exit(0)


if __name__ == '__main__':
    PORT1 = "COM18"
    PORT2 = "COM19"
    BITRATE = 115200
    # SerialRead(PORT, BITRATE)
    # CheckSerialSend(PORT, BITRATE)
    # SerialSend(PORT, BITRATE)
    # SaveSerialSend(PORT, BITRATE)
    # SaveAngleData(PORT, BITRATE)
    # MotorControl(PORT, BITRATE)
    AntagonisticControl(PORT1, PORT2, BitRate=115200)
