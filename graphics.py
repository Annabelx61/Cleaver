import pygame, gui

def draw_arrow(screen, colour, start_pos, end_pos):
    # Draw arrow line
    pygame.draw.aaline(screen, colour, start_pos, end_pos)

def draw_character(screen, position: tuple[float, float], size: int, char_id: int, image):
    """Draws the character image on the hexagon"""
    # *** NOTE: placeholder "image." no character images exist yet so it just renders the character ID!

    # Determine font size (wip)
    font = gui.font_initialization(size)
    gui.render_text(screen, font, str(char_id), position)