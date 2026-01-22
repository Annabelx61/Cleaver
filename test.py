import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import numpy as np

# Cube Direction Vectors
nw = np.array([-1, 0, 1])
w = np.array([0, -1, 1])
sw = np.array([1, -1, 0])
se = np.array([1, 0, -1])
e = np.array([0, 1, -1])
ne = np.array([-1, 1, 0])

# Vector List
vector_list = [nw, w, sw, se, e, ne]

coord = [np.array([0, 0, 0])]
for initial in coord:
    breakpoint = [np.array([-11, 11, 0])]
    is_breakpoint = np.any(np.all(initial == breakpoint, axis=1))
    if is_breakpoint == 1:
        break

    for vector in vector_list:
        newpoint = initial + vector

        is_in_coord = np.any(np.all(newpoint == coord, axis = 1))
        print(is_in_coord)
        print(newpoint)
        if is_in_coord == 0:
            coord.append(newpoint)
        print(len(coord))
colors = ["white"] * len(coord)
labels = np.arange(len(coord))

print(coord)
values = np.arange(396)
hexValues = { values:coords for (values, coords) in zip(values, coord)}

# Horizontal cartesian coords
hcoord = [c[0] for c in coord]

# Vertical cartersian coords
vcoord = [2. * np.sin(np.radians(60)) * (c[1] - c[2]) /3. for c in coord]

fig, ax = plt.subplots(1)
ax.set_aspect('equal')

# Add some coloured hexagons
for x, y, c, l in zip(hcoord, vcoord, colors, labels):
    color = c[0].lower()  # matplotlib understands lower case words for colours
    hex = RegularPolygon((x, y), numVertices=6, radius=2. / 3.,
                         orientation=np.radians(30),
                         facecolor=color, alpha=0.2, edgecolor='k')
    ax.add_patch(hex)
    # Also add a text label
    ax.text(x, y+0.2, l, ha='center', va='center', size=2)

# Also add scatter points in hexagon centres
ax.scatter(hcoord, vcoord, c=[c[0].lower() for c in colors], alpha=0.5)

plt.axis("off")
plt.show()