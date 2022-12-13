# by Matias I. Bofarull Oddo - 2022.12.07

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

mpl.use("Agg")

plt.rcParams.update({"font.sans-serif": "Consolas"})
plt.rcParams.update({"font.weight": "bold"})
plt.rcParams.update({"font.size": 10})

log_diff_threshold = 100
modulo_threshold = 25
colormap = "inferno_r"


def matrix_colormap(B_matrix, row_normalized=False):
    B_matrix = np.delete(B_matrix, (0), axis=0)
    B_matrix[B_matrix == 0.0] = np.nan
    num_rows, num_cols = np.shape(B_matrix)
    if num_rows > modulo_threshold * 100:
        ticks_Y = []
        for i in range(num_rows):
            if i % 1000 == 0:
                ticks_Y.append(i + 1)
            else:
                ticks_Y.append(" ")
    if num_rows > modulo_threshold * 10:
        ticks_Y = []
        for i in range(num_rows):
            if i % 100 == 0:
                ticks_Y.append(i + 1)
            else:
                ticks_Y.append(" ")
    elif num_rows > modulo_threshold:
        ticks_Y = []
        for i in range(num_rows):
            if i % 10 == 0:
                ticks_Y.append(i + 1)
            else:
                ticks_Y.append(" ")
    else:
        ticks_Y = []
        for i in range(num_rows):
            ticks_Y.append(i + 1)
    if num_cols > modulo_threshold * 100:
        ticks_X = []
        for i in range(num_cols):
            if i % 1000 == 0:
                ticks_X.append(i)
            else:
                ticks_X.append(" ")
    if num_cols > modulo_threshold * 10:
        ticks_X = []
        for i in range(num_cols):
            if i % 100 == 0:
                ticks_X.append(i)
            else:
                ticks_X.append(" ")
    elif num_cols > modulo_threshold:
        ticks_X = []
        for i in range(num_cols):
            if i % 10 == 0:
                ticks_X.append(i)
            else:
                ticks_X.append(" ")
    else:
        ticks_X = []
        for i in range(num_cols):
            ticks_X.append(i)
    if row_normalized:
        per_row_normalized = []
        for row in B_matrix:
            per_row_normalized.append(np.divide(row, np.nanmax(row)))
        fig = plt.figure(figsize=(9, 9))
        ax = fig.add_subplot(111)
        if np.nanmin(B_matrix) == np.nanmax(B_matrix):
            plt.pcolor(per_row_normalized, cmap=colormap, vmin=0, vmax=1)
        else:
            plt.pcolor(per_row_normalized, cmap=colormap)
    else:
        fig = plt.figure(figsize=(9, 9))
        ax = fig.add_subplot(111)
        if np.nanmax(B_matrix) - np.nanmin(B_matrix) > log_diff_threshold:
            image = plt.pcolor(
                B_matrix,
                cmap=colormap,
                norm=colors.LogNorm(
                    vmin=np.nanmin(B_matrix),
                    vmax=np.nanmax(B_matrix),
                ),
            )
        else:
            if np.nanmin(B_matrix) == np.nanmax(B_matrix):
                image = plt.pcolor(
                    B_matrix,
                    cmap=colormap,
                    vmin=np.nanmin(B_matrix) - 1,
                    vmax=np.nanmax(B_matrix),
                )
            else:
                image = plt.pcolor(
                    B_matrix,
                    cmap=colormap,
                    vmin=np.nanmin(B_matrix),
                    vmax=np.nanmax(B_matrix),
                )
        axins = inset_axes(
            ax,
            width="2%",
            height="50%",
            loc="center left",
            borderpad=-5.25,
        )
        fig.colorbar(image, cax=axins, orientation="vertical")
    ax.invert_yaxis()
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    ax.set_xticks(np.arange(len(ticks_X)) + 0.5, labels=ticks_X)
    ax.set_yticks(np.arange(len(ticks_Y)) + 0.5, labels=ticks_Y)
    if row_normalized:
        plt.savefig("BMatrix_colormap_row_norm.png", dpi=300)
    else:
        plt.savefig("BMatrix_colormap.png", dpi=300)
