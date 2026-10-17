# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 13:50:07 2022

@author: richa
"""

from hexagon import FlatTopHexagonTile, HexagonTile, CharacterTile
import pygame
import numpy as np
import gui, graphics

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

def create_character_hex(radius: float, position, character_id: int, direction: tuple[float, float]) -> CharacterTile:
    """Creates a character hexagon for the character map"""
    character_hex = CharacterTile(radius, position, character_id, direction)
    return character_hex

def hexagon_map(num_in_direction, radius, screen_size, x_offset, flat_top = True) -> list:
    """Creates a landscape of hexes centered @ 0, 0 pointing in each direction num_in_direction hexes"""
    # Pos. of center hex is defined as window size * 0.5 in both directions
    center_hexagon = create_flat_hex(position=np.array(screen_size) * np.array([0.4, 0.47]) - np.array([x_offset, 0]),
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

    return hexagons

def character_map(num_in_direction: int, radius: float, initial_pos: tuple[float, float]) -> list:
    height = np.sqrt(3) * radius
    width = 2 * radius
    character_hexagons = []

    vectors = define_vectors(width, height, flat_top = True, inverse = True)
    for i in range(len(vectors)):
        position = initial_pos + num_in_direction * vectors[i]
        direction = vectors[(i + 3) % len(vectors)]
        hexagon = create_character_hex(radius, position, len(character_hexagons), direction)

        character_hexagons.append(hexagon)

    return character_hexagons

def field_map(num_in_direction: int, radius: float, screen_size, x_offset, flat_top = True):
    map_hexagons = hexagon_map(num_in_direction, radius, screen_size, x_offset)
    char_hexagons = character_map(num_in_direction, radius, map_hexagons[0].position)

    return map_hexagons, char_hexagons


def hovered_hexagons(hexagons: list[HexagonTile]) -> list[HexagonTile]:
    mouse_pos = pygame.mouse.get_pos()
    hovered = [
        hexagon for hexagon in hexagons if hexagon.collide_with_point(mouse_pos)
    ]

    return hovered

def character_render(screen, hexagons: list[CharacterTile]):
    for hexagon in hexagons:
        hexagon.render(screen)
        hexagon.draw_direction(screen, hexagon.direction)
        graphics.draw_character(screen, hexagon.center, int(hexagon.radius), hexagon.character_id, 0)

def map_render(screen, map_hexagons):
    """Renders hexagons on the screen"""
    screen.fill((255, 255, 255))

    # global hexagons, hexagon_ids
    for hexagon in map_hexagons:
        hexagon.render(screen)

    # draw borders around colliding hexagons and neighbors
    colliding_hexagons = hovered_hexagons(map_hexagons)

    for hexagon in colliding_hexagons:
        hexagon.render_highlight(screen)

def resize(screen, event, num_in_direction):
    """Resize the window and regenerate the new resized hexagon grid."""
    screen_width, screen_height = event.size
    screen_size = screen_width, screen_height

    screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE) 

    margin = 0.1 * screen_height
    radius = (screen_height - margin)/(4 * num_in_direction + 2)

    hexagons, char_hexagons = field_map(num_in_direction, radius, screen_size, screen_size[0] * 0.1)
    return screen, hexagons, char_hexagons

def render(screen, hexagons):
    """Renders the hexagons on the screen."""
    map_render(screen, hexagons)
    pygame.display.flip()

def render_with_characters(screen, map_hexagons, char_hexagons, message, text_pos):
    """Renders the map, characters, and text."""
    font = gui.font_initialization()

    map_render(screen, map_hexagons)
    character_render(screen, char_hexagons)
    gui.render_text(screen, font, message, text_pos)

    pygame.display.flip()

def initialize():
    """ Create the resizable display, initial hexagon grid, and frame clock """
    info = pygame.display.Info()
    screen_height = info.current_h 
    screen_width = info.current_w
    screen_size = (screen_width, screen_height)

    screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE)

    margin = 0.1 * screen_height
    num_in_direction = 10
    radius = (screen_height - margin)/(4 * num_in_direction + 2)

    clock = pygame.time.Clock()

    hexagons, char_hexagons = field_map(num_in_direction, radius, screen_size, screen_width * 0.1)

    return screen, hexagons, char_hexagons, clock, num_in_direction