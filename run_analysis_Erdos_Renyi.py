# by Matias I. Bofarull Oddo - 2022.12.07

import networkx as nx
from plot_node_link import node_link

G = nx.erdos_renyi_graph(100, 3 / 99)

node_link(G)

from algorithm_BMatrix import B_Matrix

B_matrix = B_Matrix(G)

from plot_BMatrix_colormap import matrix_colormap

matrix_colormap(B_matrix, row_normalized=False)
matrix_colormap(B_matrix, row_normalized=True)

from plot_BMatrix_histogram import matrix_histogram

matrix_histogram(B_matrix, row_normalized=False)
matrix_histogram(B_matrix, row_normalized=True)
