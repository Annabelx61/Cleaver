def centered_hexagons(screen_size, flat_top=False) -> List[HexagonTile]:
    """Creates a landscape of hexes centered @ 0, 0 pointing in each direction num_in_direction hexes"""
    # Pos. of center hex is defined as window size * 0.5 in both directions
    center_hexagon = create_hexagon(position=np.array(screen_size) * np.array([0.5, 0.5]), radius = 25, flat_top=flat_top)
    size = center_hexagon.radius
    height = np.sqrt(3) * size
    width = 2 * size
    hexagons = [center_hexagon]

    # Defining vectors for hexagon tiles (flat top) clockwise
    n = np.array([0, height])
    ne = np.array([3/4 * width, 1/2 * height])
    se = np.array([3/4 * width, -1/2 * height])
    s = np.array([0, -height])
    sw = np.array([-3/4 * width, -1/2 * height])
    nw = np.array([-3/4 * width, 1/2 * height])

    vector_list = [n, ne, se, s, sw, nw]
    positions = [center_hexagon.position]
    t = 0
    for initial in hexagons:
        # Establishing endpoint
        t += 1
        if t == 518:
            break

        for vector in vector_list:
            print(initial.position)
            print(vector)
            position = initial.position + vector
            print(position)
            hexagon = create_hexagon(position = position, radius = initial.radius, flat_top = flat_top)

            # List of positions of hexagons
            is_in_list = np.any(np.all(position == positions, axis=1))
            print(is_in_list)
            if is_in_list == 0:
                positions.append(position)
                hexagons.append(hexagon)
            print(len(hexagons))

    return hexagons, positions



def centered_hexagons(num_in_direction, screen_size, flat_top=False) -> List[HexagonTile]:
    """Creates a landscape of hexes centered @ 0, 0 pointing in each direction num_in_direction hexes"""
    # Pos. of center hex is defined as window size * 0.5 in both directions
    center_hexagon = create_hexagon(position=np.array(screen_size) * np.array([0.5, 0.5]), radius = 25, flat_top=flat_top)
    size = center_hexagon.radius
    height = np.sqrt(3) * size
    width = 2 * size
    hexagons = [center_hexagon]

    # Defining vectors for hexagon tiles (flat top) clockwise
    n = np.array([0, height])
    ne = np.array([3/4 * width, 1/2 * height])
    se = np.array([3/4 * width, -1/2 * height])
    s = np.array([0, -height])
    sw = np.array([-3/4 * width, -1/2 * height])
    nw = np.array([-3/4 * width, 1/2 * height])

    vector_list = [n, ne, se, s, sw, nw]
    ring_vector_list = [se, s, sw, nw, n, ne]
    positions = [center_hexagon.position]

    for i in range(1, num_in_direction + 1):
        for j in vector_list:
            initial = center_hexagon.position + i * j
            initial_hexagon = create_hexagon(position=initial, radius=center_hexagon.radius, flat_top=flat_top)

            positions.append(initial)
            hexagons.append(initial_hexagon)

            clock = 0
            while clock < i - 1:

                k = vector_list.index(j)

                position = initial + k * clock

                hexagon = create_hexagon(position=position, radius=center_hexagon.radius, flat_top=flat_top)

                positions.append(position)
                hexagons.append(hexagon)

                clock += 1

    print(len(hexagons))
    print(len(positions))

    return hexagons, positions

