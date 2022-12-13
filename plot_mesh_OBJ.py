# by Matias I. Bofarull Oddo - 2022.12.02

# http://hdc.cs.arizona.edu/~mwli/graph-drawing/

import matplotlib.pyplot as plt


def extract_OBJ(file_path):
    vertices = []
    faces = []
    with open(file_path) as file:
        for line in file.readlines():
            values = line.split()
            if values[0] == "v":
                vX = float(values[1])
                vY = float(values[2])
                vZ = float(values[3])
                vertices.append([vX, vY, vZ])
            if values[0] == "f":
                fX = values[1].split("/")
                fY = values[2].split("/")
                fZ = values[3].split("/")
                faces.append([int(fX[0]) - 1, int(fY[0]) - 1, int(fZ[0]) - 1])
    return vertices, faces


def get_triangle(j):
    x = []
    y = []
    z = []
    for index in faces[j]:
        x.append(vertices[index][0])
        y.append(vertices[index][1])
        z.append(vertices[index][2])
    x.append(x[0])
    y.append(y[0])
    z.append(z[0])
    return x, y, z


vertices, faces = extract_OBJ("data/data_OBJ/teapot.obj")

fig = plt.figure(figsize=(9, 9))
ax = fig.add_subplot(111, projection="3d")

for i in range(len(faces)):
    x, y, z = get_triangle(i)
    ax.plot(x, y, z, color="k", linewidth=1, solid_capstyle="round")

xlim = ax.get_xlim3d()
ylim = ax.get_ylim3d()
zlim = ax.get_zlim3d()
ax.set_box_aspect((xlim[1] - xlim[0], ylim[1] - ylim[0], zlim[1] - zlim[0]))
plt.gca().set_position([0, 0, 1, 1])
plt.axis("off")
plt.show()
