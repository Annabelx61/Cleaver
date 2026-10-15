# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 13:50:07 2022

@author: richa
"""

from hexagon import FlatTopHexagonTile
from hexagon import HexagonTile

import numpy as np

def create_hexagon(tile_id, position, radius: float | int = 25, flat_top=False) -> HexagonTile:
    """Creates a hexagon tile at the specified position"""
    class_ = FlatTopHexagonTile if flat_top else HexagonTile
    return class_(radius, position, colour=(255, 255, 255), tile_id = tile_id)

def create_flat_hex(tile_id: int, position, radius: int = 25) -> HexagonTile:
    """Creates a flat top hexagon tile at the specified position"""
    hexagon = FlatTopHexagonTile(radius, position, colour = (255, 255, 255), tile_id = tile_id)
    return hexagon

def centered_hexagons(num_in_direction: int, radius: int,
                      screen_size: tuple[int, int], x_offset: float,
                      flat_top = True) -> list[HexagonTile]:
    """Creates a landscape of hexes centered @ 0, 0 pointing in each direction num_in_direction hexes"""
    # Pos. of center hex is defined as window size * 0.5 in both directions
    center_hexagon = create_hexagon(position = 0.5 * np.array(screen_size) - np.array([x_offset, 0]),
                                    radius = radius, flat_top=flat_top, tile_id = 0)
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

    vector_list = [n, ne, se] # uhat, vhat, what
    ring_vector_list = [se, s, sw] # what, -uhat, -vhat
    positions = [center_hexagon.position]

    for i in range(1, num_in_direction + 1):
        for j in range(len(vector_list)):
            initial = center_hexagon.position + i * vector_list[j]
            initial_hexagon = create_hexagon(position=initial, radius = size, flat_top=flat_top,
                                             tile_id = len(hexagons))
            mirror_pos = center_hexagon.position + i * -vector_list[j]
            mirror_hexagon = create_hexagon(position=mirror_pos, radius = size, flat_top=flat_top,
                                            tile_id=len(hexagons) + 1)

            hexagons.append(initial_hexagon)
            hexagons.append(mirror_hexagon)

            clock = 0
            while clock < i - 1:
                k = ring_vector_list[j]

                position = initial + k * (clock + 1)
                position_mirror = mirror_pos + -k * (clock + 1)

                hexagon = create_hexagon(position=position, radius=center_hexagon.radius, flat_top=flat_top,
                                         tile_id = len(hexagons))
                hexagon_mirror = create_hexagon(position=position_mirror, radius=center_hexagon.radius, flat_top=flat_top,
                                         tile_id=len(hexagons) + 1)
                hexagons.append(hexagon)
                hexagons.append(hexagon_mirror)

                clock += 1

    return hexagons, positions