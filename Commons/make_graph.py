# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 18:18:02 2019

@author: T.MATSUI
"""

import matplotlib.pyplot as plt
import csv

# カラー指定参考
# "#0033FF" : 青
# '#00FF00' : 緑
# '#FF0000' :　赤
# "#000000" : 黒

def make_graph(title_name, x_data, y_data,
                label_name, xlabel_name, ylabel_name, num_plot_data=1,
                legend_mode=False):
    color_map = ["#0033FF", '#FF0000',  "#000000"]

    plt.title(title_name, fontsize=15, fontname='Times New Roman')

    for i in range(num_plot_data):
        plt.plot(x_data, y_data[i], color=color_map[i], linestyle='solid',
                 linewidth = 1.0, label = label_name[i])

    plt.xlabel(xlabel_name, fontsize=15, fontname='Times New Roman')  # x軸のタイトル
    plt.ylabel(ylabel_name, fontsize=15, fontname='Times New Roman')  # y軸のタイトル
    if legend_mode == True:
        plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0)
    elif legend_mode == False:
        plt.legend(fontsize=10)
    plt.grid()
    plt.tight_layout()


def make_graph_two_graph(title_name, x1_data, y1_data, x2_data, y2_data, y3_data,
                         label_name, xlabel_name, ylabel_name, legend_mode=False):
    color_map = ["#0033FF", '#FF0000',  "#000000"]

    # plt.title(title_name, fontsize=15, fontname='Times New Roman')

    plt.plot(x1_data, y1_data, color=color_map[0], linestyle='solid',
             linewidth = 1.0, label = label_name[0])
    plt.plot(x2_data, y2_data, color=color_map[1], linestyle='solid',
             linewidth = 1.0, label = label_name[1])
    plt.plot(x2_data, y3_data, color=color_map[2], linestyle='solid',
             linewidth = 1.0, label = label_name[2])

    plt.xlabel(xlabel_name, fontsize=15, fontname='Times New Roman')  # x軸のタイトル
    plt.ylabel(ylabel_name, fontsize=15, fontname='Times New Roman')  # y軸のタイトル
    if legend_mode == True:
        plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0)
    elif legend_mode == False:
        plt.legend(fontsize=10)
    plt.grid()
    plt.tight_layout()

csv_dir = "csv_data/"
file_name = "kikkouLink.csv"

x_data_list, y_data_list, y_data_list2, y_data_list3, y_data_list4 = [], [], [], [], []

x1_data_list, y1_data_list, x2_data_list, y2_data_list, y3_data_list = [],[],[],[],[]
# title_name = ["qd = 90[deg]"]
title_name = ["Elastic body angle difference"]
# label_name = ["Reduced Angle", "Link Angle", "Desired Angle"]
# label_name = ["Reduced Angle(Left unit)","Reduced Angle(Right unit)" ]
label_name = ["Link Angle(Left unit)", "Link Angle(Right unit)",  "Desired Angle" ]
x_label_name = ["Time[s]"]
y_label_name = ["Angle[deg]"]

with open(csv_dir + file_name) as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        x_data = float(row[0])
        y_data = float(row[1])
        x2_data = float(row[2])
        y2_data = float(row[3])
        y3_data = float(row[4])
        #y_data_2 = float(row[2])
        #y_data_3 = float(row[3])
        # y_data_4 = float(row[4])
        x1_data_list.append(x_data)
        y1_data_list.append(y_data)
        x2_data_list.append(x2_data)
        y2_data_list.append(y2_data)
        y3_data_list.append(y3_data)
        #y_data_list2.append(y_data_2)
        #y_data_list3.append(y_data_3)
        # y_data_list4.append(y_data_4)

    data_list = [y_data_list]
    #data_list = [y_data_list, y_data_list2, y_data_list3]

    plt.figure(figsize=(6, 4))
    plt.xlim(0,14)
    plt.ylim(-50,120)
    """
    make_graph(title_name[0], x_data_list, data_list,
               label_name, x_label_name[0], y_label_name[0],
               num_plot_data=1, legend_mode=False)
    """
    make_graph_two_graph(title_name[0], x1_data_list, y1_data_list, x2_data_list, y2_data_list,
           y3_data_list, label_name, x_label_name[0], y_label_name[0], legend_mode=False)
    plt.savefig('kikkouLink.eps')
    plt.show()
