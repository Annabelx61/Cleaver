import pygame
from render import centered_hexagons

def render(screen, hexagons):
    """Renders hexagons on the screen"""
    screen.fill((255, 255, 255))
    for hexagon in hexagons:
        hexagon.render(screen)

    # draw borders around colliding hexagons and neighbours
    mouse_pos = pygame.mouse.get_pos()
    colliding_hexagons = [
        hexagon for hexagon in hexagons if hexagon.collide_with_point(mouse_pos)
    ]

    for hexagon in colliding_hexagons:
        hexagon.render_highlight(screen, border_colour=(0, 0, 0))
    pygame.display.flip()

def main():
    """Main function"""
    pygame.init()
    screen_size = (1800, 1000)
    screen = pygame.display.set_mode(screen_size)
    clock = pygame.time.Clock()
    hexagons, positions = centered_hexagons(10, 25, screen_size, screen_size[0] * 0.2)
    print(hexagons)
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