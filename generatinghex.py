import numpy as np

numlist = range(-2, 3)

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
    breakpoint = [np.array([-10, 10, 0])]
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

print(coord)

values = np.arange(396)
hexValues = { values:coords for (values, coords) in zip(values, coord)}

print(hexValues)