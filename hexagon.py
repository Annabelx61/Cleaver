# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 14:07:18 2022

@author: richa
"""
from __future__ import annotations

import math
import numpy as np
from dataclasses import dataclass

import pygame


@dataclass
class \
    HexagonTile:
    """Hexagon class"""

    radius: float
    position: tuple[float, float]
    colour: tuple[int, ...]
    highlight_offset: int = 3
    max_highlight_ticks: int = 15

    tile_id: int = 0

    def __post_init__(self):
        self.vertices = self.compute_vertices()
        self.highlight_tick = 0

    def update(self):
        """Updates tile highlights"""
        if self.highlight_tick > 0:
            self.highlight_tick -= 1

    def compute_vertices(self) -> list[tuple[float, float]]:
        """Returns a list of the hexagon's vertices as x, y tuples"""
        # pylint: disable=invalid-name
        x, y = self.position
        half_radius = self.radius / 2
        minimal_radius = self.minimal_radius
        return [
            (x, y),
            (x - minimal_radius, y + half_radius),
            (x - minimal_radius, y + 3 * half_radius),
            (x, y + 2 * self.radius),
            (x + minimal_radius, y + 3 * half_radius),
            (x + minimal_radius, y + half_radius),
        ]

    def compute_neighbors(self, hexagons: list[HexagonTile]) -> list[HexagonTile]:
        """Returns hexagons whose centers are two minimal radii away from self.centre"""
        # could cache results for performance
        return [hexagon for hexagon in hexagons if self.is_neighbor(hexagon)]

    def collide_with_point(self, point: tuple[float, float]) -> bool:
        """Returns True if distance from center to point is less than horizontal_length"""
        return math.dist(point, self.centre) < self.minimal_radius

    def is_neighbor(self, hexagon: HexagonTile) -> bool:
        """Returns True if hexagon center is approximately
        2 minimal radii away from own center
        """
        distance = math.dist(hexagon.centre, self.centre)
        return math.isclose(distance, 2 * self.minimal_radius, rel_tol=0.05)

    def render(self, screen) -> None:
        """Renders the hexagon on the screen"""
        pygame.draw.polygon(screen, self.colour, self.vertices)
        pygame.draw.aalines(screen, (0, 0, 0), closed=True, points=self.vertices)

    def render_highlight(self, screen) -> None:
        """Draws a border around the hexagon with the specified color"""
        self.highlight_tick = self.max_highlight_ticks
        pygame.draw.polygon(screen, self.highlight_colour, self.vertices)
        pygame.draw.aalines(screen, (0, 0, 0), closed=True, points=self.vertices)

    @property
    def centre(self) -> tuple[float, float]:
        """Center of the hexagon"""
        x, y = self.position  # pylint: disable=invalid-name
        return x, y + self.radius

    @property
    def minimal_radius(self) -> float:
        """Horizontal length of the hexagon"""
        # https://en.wikipedia.org/wiki/Hexagon#Parameters
        return self.radius * math.cos(math.radians(30))

    @property
    def highlight_colour(self) -> tuple[int, ...]:
        """Color of the hexagon tile when rendering highlight"""
        #offset = self.highlight_offset * self.highlight_tick
        #brighten = lambda x, y: x + y if x + y < 255 else 255

        light_blue = (179, 251, 255)

        return light_blue

class FlatTopHexagonTile(HexagonTile):
    def compute_vertices(self) -> list[tuple[float, float]]:
        """Returns a list of the hexagon's vertices as x, y tuples"""
        # pylint: disable=invalid-name
        x, y = self.position
        half_radius = self.radius / 2
        minimal_radius = self.minimal_radius
        return [
            (x, y),
            (x - half_radius, y + minimal_radius),
            (x, y + 2 * minimal_radius),
            (x + self.radius, y + 2 * minimal_radius),
            (x + 3 * half_radius, y + minimal_radius),
            (x + self.radius, y),
        ]

    @property
    def centre(self) -> tuple[float, float]:
        """Center of the hexagon"""
        x, y = self.position  # pylint: disable=invalid-name
        return x + self.radius / 2, y + self.minimal_radius

@dataclass
class CharacterTile:
    """Character tile that lies on top of bottom hexagon map"""

    radius: float
    position: tuple[float, float]

    character_id: int
    direction: tuple[float, float]

    def __post_init__(self):
        self.vertices = self.compute_vertices()
        self.highlight_tick = 0

    def compute_vertices(self) -> list[tuple[float, float]]:
        """Returns a list of the hexagon's vertices as x, y tuples"""
        x, y = self.position
        half_radius = self.radius / 2
        minimal_radius = self.minimal_radius
        return [
            (x, y),
            (x - half_radius, y + minimal_radius),
            (x, y + 2 * minimal_radius),
            (x + self.radius, y + 2 * minimal_radius),
            (x + 3 * half_radius, y + minimal_radius),
            (x + self.radius, y),
        ]

    def compute_arrow_vertices(self, edge_center, vector) -> list[tuple[float, float]]:
        # Defining rotation matrix
        theta = math.radians(120)
        rotation_matrix = np.array([[math.cos(theta), -math.sin(theta)],
                                   [math.sin(theta), math.cos(theta)]])

        # Initial point adjustment and application of rotation matrix once for vertex2 and twice for vertex3
        vertex1 = np.array([0.15 * vector[0], 0.15 * vector[1]])
        vertex2 = rotation_matrix @ vertex1
        vertex3 = rotation_matrix @ vertex2
        vertices = vertex1, vertex2, vertex3

        # Adjusting each vertex to centroid
        vertices = [
            (vertex + edge_center) for vertex in vertices
        ]

        return vertices

    def render(self, screen):
        """Renders the hexagon on the screen"""
        pygame.draw.polygon(screen, self.highlight_color, self.vertices)
        pygame.draw.aalines(screen, (0, 0, 0), closed=True, points=self.vertices)

    def draw_direction(self, screen, direction):
        """Draws the vector arrow for the direction"""
        edge_center = self.edge_center(direction)
        pygame.draw.polygon(screen, (0, 0, 0), self.compute_arrow_vertices(edge_center, direction))

    def edge_center(self, vector) -> tuple[float, float]:
        """Finds position of the center of the edge of a hex, in the specified direction"""
        edge_pos = self.center + (0.5 * vector)
        return edge_pos

    @property
    def center(self) -> tuple[float, float]:
        """Center of the hexagon"""
        x, y = self.position  # pylint: disable=invalid-name
        return x + self.radius / 2, y + self.minimal_radius

    @property
    def minimal_radius(self) -> float:
        """Horizontal length of the hexagon"""
        # https://en.wikipedia.org/wiki/Hexagon#Parameters
        return self.radius * math.cos(math.radians(30))

    @property
    def highlight_color(self) -> tuple[int, ...]:
        """Highlight color, depending on enemy vs. player"""
        if self.character_id == 0:
            blue = (180, 200, 255)
            return blue
        else:
            red = (255, 200, 200)
            return red