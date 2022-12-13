# by Matias I. Bofarull Oddo - 2022.12.07

import networkx as nx
from plot_node_link import node_link

files = [
    "bunny",
    "camel",
    "cube",
    "cyl1",
    "cyl2",
    "icos",
    "sphere1",
    "teapot",
    "tet",
]

filename = files[7]

with open("data/data_OBJ/" + filename + ".obj") as file:
    faces = []
    for line in file.readlines():
        values = line.split()
        if values[0] == "f":
            row = []
            for triplet in values[1:]:
                pointers = triplet.split("/")
                row.append(pointers[0])
            faces.append(row)
file.close()

with open("data/data_OBJ/" + filename + ".csv", "w") as csv_file:
    for face in faces:
        csv_file.write(str(face[0]) + "," + str(face[1]) + "\n")
        csv_file.write(str(face[1]) + "," + str(face[2]) + "\n")

csv_file.close()

G = nx.read_edgelist(
    "data/data_OBJ/" + filename + ".csv",
    delimiter=",",
    nodetype=str,
)

node_link(G)

from algorithm_BMatrix import B_Matrix

B_matrix = B_Matrix(G)

from plot_BMatrix_colormap import matrix_colormap

matrix_colormap(B_matrix, row_normalized=False)
matrix_colormap(B_matrix, row_normalized=True)

from plot_BMatrix_histogram import matrix_histogram

matrix_histogram(B_matrix, row_normalized=False)
matrix_histogram(B_matrix, row_normalized=True)
