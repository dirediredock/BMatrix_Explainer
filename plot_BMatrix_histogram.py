# by Matias I. Bofarull Oddo - 2022.12.07

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use("Agg")

plt.rcParams.update({"font.sans-serif": "Consolas"})
plt.rcParams.update({"font.weight": "bold"})
plt.rcParams.update({"font.size": 10})

log_diff_threshold = 100
modulo_threshold = 25


def matrix_histogram(B_matrix, row_normalized=True):
    B_matrix = np.delete(B_matrix, (0), axis=0)
    B_matrix[B_matrix == 0.0] = np.nan
    num_rows, num_cols = np.shape(B_matrix)
    if num_cols > modulo_threshold * 100:
        ticks_X = []
        for i in range(num_cols):
            if i % 1000 == 0:
                ticks_X.append(i)
            else:
                ticks_X.append(" ")
    elif num_cols > modulo_threshold * 10:
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
    empty_ticks_X = []
    for i in range(num_cols):
        empty_ticks_X.append("")
    fig = plt.figure(figsize=(9, 9))
    for i in range(len(B_matrix)):
        row = B_matrix[i]
        ax = fig.add_subplot(len(B_matrix), 1, i + 1)
        ax.bar(range(len(ticks_X)), row, color="k")
        ax.set_xlim([-0.65, num_cols])
        if row_normalized:
            ax.set_ylim([0, np.nanmax(row)])
            ax.set_yticks(np.arange(0, np.nanmax(row) + 1, np.nanmax(row)))
            ax.text(
                num_cols,
                np.nanmax(row) * 0.5,
                " " + str(i + 1),
                ha="left",
                va="center",
            )
            if i == 0:
                ax.spines["bottom"].set_visible(False)
                plt.setp(ax.get_yticklabels()[0], visible=False)
                plt.setp(ax.get_yticklines()[0], visible=False)
                ax.get_xaxis().set_ticks([])
            elif i + 1 == num_rows:
                ax.spines["top"].set_visible(False)
                ax.set_xticks(np.arange(len(ticks_X)), labels=ticks_X)
            else:
                ax.spines["top"].set_visible(False)
                ax.spines["bottom"].set_visible(False)
                plt.setp(ax.get_yticklabels()[0], visible=False)
                plt.setp(ax.get_yticklines()[0], visible=False)
                ax.get_xaxis().set_ticks([])
        else:
            ax.set_ylim([0, np.nansum(row)])
            ax.set_yticks(np.arange(0, np.nansum(row) + 1, np.nansum(row)))
            ax.text(
                num_cols,
                np.nansum(row) * 0.5,
                " " + str(i + 1),
                ha="left",
                va="center",
            )
            if i == 0:
                ax.spines["bottom"].set_visible(False)
                plt.setp(ax.get_yticklabels()[0], visible=False)
                plt.setp(ax.get_yticklines()[0], visible=False)
                ax.get_xaxis().set_ticks([])
            elif i + 1 == num_rows:
                ax.spines["top"].set_visible(False)
                ax.set_xticks(np.arange(len(ticks_X)), labels=ticks_X)
                ax.get_yaxis().set_ticks([])
            else:
                ax.spines["top"].set_visible(False)
                ax.spines["bottom"].set_visible(False)
                ax.get_xaxis().set_ticks([])
                ax.get_yaxis().set_ticks([])
        ax.axhline(y=0, color="silver", zorder=-1)
    fig.subplots_adjust(hspace=0)
    if row_normalized:
        plt.savefig("BMatrix_histogram_row_norm.png", dpi=300)
    else:
        plt.savefig("BMatrix_histogram.png", dpi=300)
