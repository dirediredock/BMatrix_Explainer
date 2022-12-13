# by Matias I. Bofarull Oddo - 2022.12.08

import networkx as nx
from plot_node_link import node_link

# G = nx.Graph(nx.read_pajek("data/data_CSV/USAir97.net"))

# G = nx.read_edgelist("data/data_CSV/infobox_network_Fortran.tsv")
# G.remove_edges_from(nx.selfloop_edges(G))

G = nx.read_edgelist("data/data_CSV/infobox_network_Carl_Jung.tsv")
G.remove_edges_from(nx.selfloop_edges(G))

node_link(G)

from algorithm_BMatrix import B_Matrix

B_matrix = B_Matrix(G)

from plot_BMatrix_colormap import matrix_colormap

matrix_colormap(B_matrix, row_normalized=False)
matrix_colormap(B_matrix, row_normalized=True)

from plot_BMatrix_histogram import matrix_histogram

matrix_histogram(B_matrix, row_normalized=False)
matrix_histogram(B_matrix, row_normalized=True)
