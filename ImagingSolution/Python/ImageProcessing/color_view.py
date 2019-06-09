# -*- coding: utf-8 -*-
"""
Created on Tue Jul 25 17:12:25 2017

@author: sakurai
"""

import matplotlib.pyplot as plt
import numpy as np


if __name__ == '__main__':
    num_classes = 11
    num_max_segments = 40
    mean_segment_length = 5
    random = False

    # gerate data (i.e. a sequence of segments integers)
    if random:
        segments = np.random.choice(num_classes, num_max_segments)
    else:
        segments = np.arange(num_classes)
    durations = np.random.randint(3, 6, num_max_segments)
    labels = []
    for label, duration in zip(segments, durations):
        labels += [label] * duration
    labels = np.ravel(labels)
    print('labels:', labels)
    seq_len = len(labels)

#     # gist_ncar or tab20 seem good.
#    colors = plt.cm.gist_ncar(np.linspace(0, 1, num_classes))
#    for t, label in enumerate(labels):
#        plt.axvspan(t, t + 1, color=colors[label])
#    plt.xlim(0, seq_len)
#    plt.show()

    # iterate through all cmap classes
    cmaps = {}
    for name, cmap in plt.cm.__dict__.items():
        if isinstance(cmap, plt.matplotlib.colors.Colormap):
            cmaps[name] = cmap

    for name, cmap in sorted(cmaps.items()):
        print(name)
        colors = cmap(np.linspace(0, 1, num_classes))
        for t, label in enumerate(labels):
            plt.axvspan(t, t + 1, color=colors[label], lw=0)
        plt.title(name)
        plt.xlim(0, seq_len)
        plt.show()

    print('labels:', labels)