import pygame
from render import field_map, map_render, character_render, render
from text import text_initialization, render_text

def main():
    """Main function"""
    pygame.init()
    screen_size = (1900, 1000)
    screen = pygame.display.set_mode(screen_size)
    screen_center = tuple([0.5 * i for i in screen_size])
    clock = pygame.time.Clock()
    hexagons, character_hexagons = field_map(10, 25, screen_size, screen_size[0] * 0.2)
    font = text_initialization()
    terminated = False

    mouse_pos = (0, 0)
    while not terminated:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminated = True

        for hexagon in hexagons:
            hexagon.update()

        mouse_clicked = pygame.mouse.get_pressed(3)
        if mouse_clicked[0]:
            mouse_pos = pygame.mouse.get_pos()

        map_render(screen, hexagons)
        character_render(screen, character_hexagons)
        render_text(font, str(mouse_pos), (0, 0), screen)

        render(screen, hexagons, character_hexagons, str(mouse_pos), screen_center)
        clock.tick(50)
    pygame.display.quit()


if __name__ == "__main__":
    main()