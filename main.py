import pygame
from render import centered_hexagons, render

def main():
    """Main function"""
    pygame.init()
    screen_size = (1620, 900)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    hexagons, positions = centered_hexagons(10, 25, screen_size, screen_size[0] * 0.2)
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