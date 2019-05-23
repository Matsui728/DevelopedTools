# -*- coding: utf-8 -*-
"""
Created on Wed May 22 17:18:39 2019

@author: T.MATSUI
"""

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def array_info(x):
    print("配列のshape", x.shape)
    print("配列の要素のデータ型", x.dtype)
    if len(x) >= 10:
        print("配列の中身（上から10列）\n", x[:10], "\n")
    else:
        print("配列の中身\n", x, "\n")


def MakeHeatmap(HeatMapData):
    data = np.loadtxt(HeatMapData, delimiter=',')
    array_info(data)
    sns.heatmap(data, robust="True")


if __name__ == '__main__':

    data = np.loadtxt('data/sample2.csv', delimiter=',')
    array_info(data)
    MakeHeatmap(data)
    
