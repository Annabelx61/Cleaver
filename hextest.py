# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 13:50:07 2022

@author: richa
"""
import random
from typing import List
from typing import Tuple

import pygame
from hexagon import FlatTopHexagonTile
from hexagon import HexagonTile

import numpy as np
# pylint: disable=no-member

# Loading PyGame images

def create_hexagon(tile_id, position, radius=25, flat_top=False) -> HexagonTile:
    """Creates a hexagon tile at the specified position"""
    class_ = FlatTopHexagonTile if flat_top else HexagonTile
    return class_(radius, position, colour=(255, 255, 255), tile_id = tile_id)


def get_random_colour(min_=150, max_=255) -> Tuple[int, ...]:
    """Returns a random RGB colour with each component between min_ and max_"""
    return tuple(random.choices(list(range(min_, max_)), k=3))


def init_hexagons(num_x=25, num_y=25, flat_top=False) -> List[HexagonTile]:
    """Creates a hexaogonal tile map of size num_x * num_y"""
    # pylint: disable=invalid-name
    leftmost_hexagon = create_hexagon(position=(-50, -50), flat_top=flat_top)
    hexagons = [leftmost_hexagon]
    for x in range(num_y):
        if x:
            # alternate between bottom left and bottom right vertices of hexagon above
            index = 2 if x % 2 == 1 or flat_top else 4
            position = leftmost_hexagon.vertices[index]
            leftmost_hexagon = create_hexagon(position, flat_top=flat_top)
            hexagons.append(leftmost_hexagon)

        # place hexagons to the left of leftmost hexagon, with equal y-values.
        hexagon = leftmost_hexagon
        for i in range(num_x):
            x, y = hexagon.position  # type: ignore
            if flat_top:
                if i % 2 == 1:
                    position = (x + hexagon.radius * 3 / 2, y - hexagon.minimal_radius)
                else:
                    position = (x + hexagon.radius * 3 / 2, y + hexagon.minimal_radius)
            else:
                position = (x + hexagon.minimal_radius * 2, y)
            hexagon = create_hexagon(position, flat_top=flat_top)
            hexagons.append(hexagon)

    return hexagons


def centered_hexagons(num_in_direction, screen_size, x_offset, flat_top=False) -> List[HexagonTile]:
    """Creates a landscape of hexes centered @ 0, 0 pointing in each direction num_in_direction hexes"""
    # Pos. of center hex is defined as window size * 0.5 in both directions
    center_hexagon = create_hexagon(position=np.array(screen_size) * np.array([0.5, 0.5]) - np.array([x_offset, 0]),
                                    radius = 25, flat_top=flat_top, tile_id = 0)
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
        for j in range(len(vector_list)):
            initial = center_hexagon.position + i * vector_list[j]
            initial_hexagon = create_hexagon(position=initial, radius=center_hexagon.radius, flat_top=flat_top,
                                             tile_id = len(hexagons))

            positions.append(initial)
            hexagons.append(initial_hexagon)

            clock = 0
            while clock < i - 1:

                k = ring_vector_list[j]

                position = initial + k * (clock + 1)

                hexagon = create_hexagon(position=position, radius=center_hexagon.radius, flat_top=flat_top,
                                         tile_id = len(hexagons))

                positions.append(position)
                hexagons.append(hexagon)

                clock += 1

    return hexagons, positions

def render(screen, hexagons):
    """Renders hexagons on the screen"""
    screen.fill((255, 255, 255))
    for hexagon in hexagons:
        hexagon.render(screen)

    # draw borders around colliding hexagons and neighbours
    mouse_pos = pygame.mouse.get_pos()
    colliding_hexagons = [
        hexagon for hexagon in hexagons if hexagon.collide_with_point(mouse_pos)
    ]

    for hexagon in colliding_hexagons:
        hexagon.render_highlight(screen, border_colour=(0, 0, 0))
    pygame.display.flip()

def render_text(message, font, color, x, y):
    surface = font.render(message, True, color)
    screen.blit(img, (x, y))

def main():
    """Main function"""
    pygame.init()
    screen_size = (1800, 1000)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    hexagons, positions = centered_hexagons(10, screen_size, screen_size[0] * 0.2, flat_top=True)
    print(hexagons)
    terminated = False

    while not terminated:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminated = True

        for hexagon in hexagons:
            hexagon.update()

        render(screen, hexagons)
        clock.tick(50)
    pygame.display.quit()


if __name__ == "__main__":
    main()