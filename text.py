import pygame

def text_initialization():
    font = pygame.font.SysFont("Times New Roman", 36)
    return font

def render_text(font, message: str, position: tuple[float, float], screen):
    text = font.render(message, False, (0, 0, 0))
    screen.blit(text, position)