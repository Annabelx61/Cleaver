import pygame

def draw_arrow(screen, colour, start_pos, end_pos):
    # Draw arrow line
    pygame.draw.aaline(screen, colour, start_pos, end_pos)

