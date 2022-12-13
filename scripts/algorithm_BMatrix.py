# Modified by Matias I. Bofarull Oddo - 2022.11.28
# From Jim Bagrow github.com/bagrow/portraits - 2021.05.06
# Original B-Matrix concept in DOI 10.1209/0295-5075/81/68004 - 2008.04.21

import numpy as np


def B_Matrix(G):
    diameter = 1000
    array = zeroes_array((diameter + 1, G.number_of_nodes()))
    max_path = 1
    adjencent_nodes = G.adj
    for starting_node in G.nodes():
        nodes_visited = {starting_node: 0}
        search_queue = [starting_node]
        count = 1
        while search_queue:
            next_depth = []
            extend = next_depth.extend
            for n in search_queue:
                l = [i for i in adjencent_nodes[n] if i not in nodes_visited]
                extend(l)
                for j in l:
                    nodes_visited[j] = count
            search_queue = next_depth
            count += 1
        node_distances = nodes_visited.values()
        max_node_distances = max(node_distances)
        curr_max_path = max_node_distances
        if curr_max_path > max_path:
            max_path = curr_max_path
        dict_distribution = dict.fromkeys(node_distances, 0)
        for count in node_distances:
            dict_distribution[count] += 1
        for shell, count in dict_distribution.items():
            array[shell][count] += 1
        max_shell = diameter
        while max_shell > max_node_distances:
            array[max_shell][0] += 1
            max_shell -= 1
    B_matrix = array[: max_path + 1, :]
    trim = np.where(B_matrix != 0)
    B_matrix = B_matrix[
        0 : max(trim[0]) + 1,
        0 : max(trim[1]) + 1,
    ]
    return B_matrix


def logarithmic_colormap(mattrix):
    new_matrix = zeroes_array(mattrix.shape, data_type=float)
    i = 0
    for row in mattrix:
        j = 0
        for value in row:
            if value != 0:
                new_matrix[i, j] = np.log(value + 1)
            else:
                new_matrix[i, j] = 0
            j += 1
        i += 1
    return new_matrix


def zeroes_array(shape, data_type=None):
    try:
        return np.zeros(shape, dtype=data_type)
    except TypeError:
        return np.zeros(shape, typecode="fd")


"""
    See https://github.com/bagrow/portraits/blob/master/B_matrix.py

    COPYRIGHT

        Copyright (C) 2008-2021 Jim Bagrow. This program is free software; you
        can redistribute it and/or modify it under the terms of the GNU General
        Public License as published by the Free Software Foundation; either
        version 2 of the License, or (at your option) any later version. This
        program is distributed in the hope that it will be useful, but WITHOUT
        ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
        FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
        for more details. You should have received a copy of the GNU General
        Public License along with this program; if not, write to the Free
        Software Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
        02111-1307 USA.
        
        See http://www.gnu.org/licenses/gpl.txt for more details.

    ABOUT

        Plot complex networks portraits, requires python 2.4 (I think?),
        networkx, and (optionally) matplotlib/pylab for plotting. If this
        software is used in an article, an acknowledgment would be awesome,
        as would an email with the article. Please cite as:

            J. P. Bagrow et al 2008 EPL 81 68004

    DEPENDANCIES

        http://www.python.org/
        https://networkx.lanl.gov/
        http://matplotlib.sourceforge.net/

    REFERENCES
        
        http://people.clarkson.edu/~qd00/B_matrix_site/
        http://arxiv.org/abs/cond-mat/0703470v2

            DOI 10.1209/0295-5075/81/68004
        
    Jim Bagrow, 2008-04-21
    bagrowjp [at] gmail [dot] com
"""
