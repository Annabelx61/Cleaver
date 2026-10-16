import pygame
from render import centered_hexagons
import render

def main():
    """Main function"""
    pygame.init()
    screen, hexagons, clock, num_in_direction = render.initialize()
    terminated = False

    mouse_pos = (0, 0)
    while not terminated:
        for event in pygame.event.get():
            # quit event
            if event.type == pygame.QUIT:
                terminated = True
            # resize window
            elif event.type == pygame.VIDEORESIZE:
                screen, hexagons = render.resize(screen,event, num_in_direction)
        for hexagon in hexagons:
            hexagon.update()
        render.render(screen, hexagons)
        clock.tick(50)
    pygame.display.quit()


if __name__ == "__main__":
    main()