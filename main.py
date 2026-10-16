import pygame
import render


def main():
    """Main function."""
    pygame.init()
    screen, hexagons, char_hexagons, clock, num_in_direction = render.initialize()
    terminated = False

    while not terminated:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminated = True
            elif event.type == pygame.VIDEORESIZE:
                screen, hexagons, char_hexagons = render.resize(screen, event, num_in_direction)
        for hexagon in hexagons:
            hexagon.update()
        render.map_render(screen, hexagons)
        render.character_render(screen, char_hexagons)
        pygame.display.flip()
        clock.tick(50)
    pygame.quit()


if __name__ == "__main__":
    main()