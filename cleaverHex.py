'''
Created on Sun Jan 4 2026

Mostly rewriting code from hexagon.py so I can better understand what
is actually happening and modify it from there.
'''
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import List
from typing import Tuple

import pygame

@dataclass
class HexagonTile:
    """Hexagon class"""

    radius: float
    position: Tuple[float, float]
    color: Tuple[int, ...]
    highlight_offset: int = 3
    max_highlight_ticks: int = 15


    def __post_init__(self):
        self.vertices = self.compute vertices()
        self.highlight_tick = 0

    def update(self):
        # Updates tile highlights
        if self.highlight_tick > 0:
            self.highlight_tick -= 1

    def compute_vertices(self) -> List[Tuple[float, float]]:
        """Returns a list of the hexagon's vertices as x, y tuples"""
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