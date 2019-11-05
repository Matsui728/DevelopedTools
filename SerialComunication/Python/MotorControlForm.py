# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 15:48:48 2019

@author: T.Matsui
"""

import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from tkinter import font


def MakeForm(title_name):
    root = tk.Tk()
    root.wm_title(title_name)  # ウインドウネーム作成
    root.geometry("1280x960")  # フォームサイズ指定
    root.configure(bg='midnightblue')
    return root


def MakeCanvas(root):
    # グラフ用fig生成
    fig1 = Figure(figsize=(6, 4))
    fig2 = Figure(figsize=(6, 4))
    fig3 = Figure(figsize=(6, 4))
    fig4 = Figure(figsize=(6, 4))
    fig5 = Figure(figsize=(6, 4))
    fig6 = Figure(figsize=(6, 4))
    fig = [fig1, fig2, fig3, fig4, fig5, fig6]

    canvas1 = FigureCanvasTkAgg(fig1, master=root)    # フォームキャンバス作成
    canvas2 = FigureCanvasTkAgg(fig2, master=root)    # フォームキャンバス作成
    canvas3 = FigureCanvasTkAgg(fig3, master=root)    # フォームキャンバス作成
    canvas4 = FigureCanvasTkAgg(fig4, master=root)    # フォームキャンバス作成
    canvas5 = FigureCanvasTkAgg(fig5, master=root)    # フォームキャンバス作成
    canvas6 = FigureCanvasTkAgg(fig6, master=root)    # フォームキャンバス作成

    canvas = [canvas1, canvas2, canvas3, canvas4, canvas5, canvas6]
    return fig, canvas


def init1():  # only required for blitting to give a clean slate.
    line1.set_ydata(np.sin(x))
    return line1,


def init2():  # only required for blitting to give a clean slate.
    line2.set_ydata(np.sin(x))
    return line2,


def init3():  # only required for blitting to give a clean slate.
    line3.set_ydata(np.sin(x))
    return line3,


def init4():  # only required for blitting to give a clean slate.
    line4.set_ydata(np.sin(x))
    return line4,


def init5():  # only required for blitting to give a clean slate.
    line5.set_ydata(np.sin(x))
    return line5,


def init6():  # only required for blitting to give a clean slate.
    line6.set_ydata(np.sin(x))
    return line6,


def animate1(i):
    line1.set_ydata(np.sin(x + i))  # update the data.
    return line1,


def animate2(i):
    line2.set_ydata(np.sin(x + i))  # update the data.
    return line2,


def animate3(i):
    line3.set_ydata(np.sin(x + i))  # update the data.
    return line3,


def animate4(i):
    line4.set_ydata(np.sin(x + i))  # update the data.
    return line4,


def animate5(i):
    line5.set_ydata(np.sin(x + i))  # update the data.
    return line5,


def animate6(i):
    line6.set_ydata(np.sin(x + i))  # update the data.
    return line6,


def _CheckEncoder():
    # Make later

    return 0


def _MotorControl():
    # Make later

    return 0


# プログラム終了ボタン処理
def _quit():
    root.quit()         # main loop を止める
    root.destroy()      # Windows上でプログラム終了には必要


def _start():
    # Make later
    return 0


if __name__ == '__main__':
    root = MakeForm("Motor Control")
    font1 = font.Font(family='Times New Roman', size=20, weight='bold')
    fig, canvas = MakeCanvas(root)

    x = np.arange(0, 3, 0.01)  # x軸(固定の値)
    ll = np.arange(0, 8, 0.01)  # 表示期間(FuncAnimationで指定する関数の引数になる)

    plot_data = fig[0].add_subplot(111)
    plot_data.set_ylim([-1.1, 1.1])
    line1, = plot_data.plot(x, np.sin(x))
    ani1 = animation.FuncAnimation(fig[0], animate1, ll,
                                   init_func=init1, interval=50, blit=True,)

    plot_data2 = fig[1].add_subplot(111)
    plot_data2.set_ylim([-1.1, 1.1])
    line2, = plot_data2.plot(x, np.sin(x))
    ani2 = animation.FuncAnimation(fig[1], animate2, ll,
                                   init_func=init2, interval=50, blit=True,)

    plot_data3 = fig[2].add_subplot(111)
    plot_data3.set_ylim([-1.1, 1.1])
    line3, = plot_data3.plot(x, np.sin(x))
    ani3 = animation.FuncAnimation(fig[2], animate3, ll,
                                   init_func=init3, interval=50, blit=True,)

    plot_data4 = fig[3].add_subplot(111)
    plot_data4.set_ylim([-1.1, 1.1])
    line4, = plot_data4.plot(x, np.sin(x))
    ani4 = animation.FuncAnimation(fig[3], animate4, ll,
                                   init_func=init4, interval=50, blit=True,)

    plot_data5 = fig[4].add_subplot(111)
    plot_data5.set_ylim([-1.1, 1.1])
    line5, = plot_data5.plot(x, np.sin(x))
    ani5 = animation.FuncAnimation(fig[4], animate5, ll,
                                   init_func=init5, interval=50, blit=True,)

    plot_data6 = fig[5].add_subplot(111)
    plot_data6.set_ylim([-1.1, 1.1])
    line6, = plot_data6.plot(x, np.sin(x))
    ani6 = animation.FuncAnimation(fig[5], animate6, ll,
                                   init_func=init6, interval=50, blit=True,)

    toolbar = NavigationToolbar2TkAgg(canvas[0], root)

    canvas[0].get_tk_widget().place(x=400, y=90)
    canvas[1].get_tk_widget().place(x=400, y=360)
    canvas[2].get_tk_widget().place(x=400, y=630)
    canvas[3].get_tk_widget().place(x=800, y=90)
    canvas[4].get_tk_widget().place(x=800, y=360)
    canvas[5].get_tk_widget().place(x=800, y=630)

    Static1 = tk.Label(text=u"Please Select Control Mode.",
                       foreground="#00ff00", background="midnightblue",
                       font=font1)
    Static1.place(x=40, y=30)

    # Encoder Chacker
    encoder_check_button = tk.Button(master=root, text="Encoder Check Mode",
                                     width=20, height=3, command=_CheckEncoder)
    encoder_check_button.place(x=70, y=90)

    # motor_control
    motor_control_button = tk.Button(master=root, text="Motor Control Mode",
                                     width=20, height=3, command=_CheckEncoder)
    motor_control_button.place(x=230, y=90)

    # 制御開始ボタン
    start_button = tk.Button(master=root, text="Plogram Start!",  width=20,
                             height=3, command=_start)
    start_button.place(x=80, y=430)

    # 終了ボタン配置
    quit_button = tk.Button(master=root, text="Quit", width=20, height=3,
                            command=_quit)
    quit_button.place(x=240, y=430)

    tk.mainloop()
