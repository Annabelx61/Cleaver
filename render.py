# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 13:50:07 2022

@author: richa
"""

from hexagon import FlatTopHexagonTile
from hexagon import HexagonTile
import pygame
import numpy as np

def define_vectors(width: float, height: float, flat_top: bool, inverse: bool = False) -> list:
    """Defines hexagon directional vectors based on flat_top"""
    if flat_top:
        uhat = np.array([0, height])
        vhat = np.array([3 / 4 * width, 1 / 2 * height])
        what = np.array([3 / 4 * width, -1 / 2 * height])
        vectors = [uhat, vhat, what]
    else:
        uhat = np.array([width, 0])
        vhat = np.array([1/2 * width, 3/4 * height])
        what = np.array([-1/2 * width, 3/4 * height])
        vectors = [uhat, vhat, what]

    if inverse:
        vectors_inverse = [-i for i in vectors]
        vectors.extend(vectors_inverse)

    return vectors

def create_flat_hex(tile_id: int, position, radius: int | float = 25) -> HexagonTile:
    """Creates a flat top hexagon tile at the specified position"""
    hexagon = FlatTopHexagonTile(radius, position, colour = (255, 255, 255), tile_id = tile_id)
    return hexagon

def centered_hexagons(num_in_direction, radius, screen_size, x_offset, flat_top = True):
    """Creates a landscape of hexes centered @ 0, 0 pointing in each direction num_in_direction hexes"""
    # Pos. of center hex is defined as window size * 0.5 in both directions
    center_hexagon = create_flat_hex(position=np.array(screen_size) * np.array([0.5, 0.5]) - np.array([x_offset, 0]),
                                    radius = radius, tile_id = 0)
    height = np.sqrt(3) * radius
    width = 2 * radius
    hexagons = [center_hexagon]

    vectors = define_vectors(width, height, flat_top = flat_top, inverse = True)
    for i in range(1, num_in_direction + 1): # 1 to +1 to avoid recounting initial center hexagon
        for j in range(len(vectors)):
            initial = center_hexagon.position + i * vectors[j] # Creates the 'spines,' num in all direct vectors
            initial_hexagon = create_flat_hex(position = initial, radius = radius, tile_id = len(hexagons))
            hexagons.append(initial_hexagon)

            clock = 0
            index = (j + 2) % len(vectors) # Keeping index in bounds, 2 ahead of the 'spine' vector
            while clock < i - 1:
                position = initial + vectors[index] * (clock + 1) # Finds each hex up to the edge of the next 'spine'
                hexagon = create_flat_hex(position = position, radius = radius, tile_id = len(hexagons))
                hexagons.append(hexagon)
                clock += 1

    positions = [hexagon.position for hexagon in hexagons] # A list of all hexagon positions

    return hexagons, positions

def hovered_hexagons(hexagons: list[HexagonTile]) -> list[HexagonTile]:
    mouse_pos = pygame.mouse.get_pos()
    hovered = [
        hexagon for hexagon in hexagons if hexagon.collide_with_point(mouse_pos)
    ]

    return hovered

def render(screen, input_hexagons):
    """Renders hexagons on the screen"""
    screen.fill((255, 255, 255))

    hexagons = input_hexagons
    hexagon_ids = [hexagon.tile_id for hexagon in input_hexagons]

    global hexagons, hexagon_ids
    for hexagon in hexagons:
        hexagon.render(screen)

    # draw borders around colliding hexagons and neighbours
    colliding_hexagons = hovered_hexagons(hexagons)

    for hexagon in colliding_hexagons:
        hexagon.render_highlight(screen)

    mouse_clicked = pygame.mouse.get_pressed(3)
    # if mouse_clicked:
    #     hex_id = colliding_hexagons[0].tile_id
    #     index = hexagon_ids.index(hex_id)
    #     hexagons

    # selected_hexagons = [
    #     hexagon if hexagon.is_selected for hexagon in hexagons
    # ]

    pygame.display.flip()