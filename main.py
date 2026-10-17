import pygame
import render, gui


def main():
    """Main function."""
    pygame.init()
    screen, hexagons, char_hexagons, clock, num_in_direction = render.initialize()
    terminated = False

    objects = gui.main_menu(screen)
    while not terminated:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminated = True
            elif event.type == pygame.VIDEORESIZE:
                screen, hexagons, char_hexagons = render.resize(screen, event, num_in_direction)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for item in objects:
                    if isinstance(item, gui.InputBox): # Checks to see if its type InputBox before running InputBox functionality
                        item.handle_event(event)
            elif event.type == pygame.KEYDOWN:
                for item in objects: # Loops over each object returned by the menu function
                    if isinstance(item, gui.InputBox): # Checks to see if its type InputBox before running InputBox functionality
                        item.handle_event(event)


        for hexagon in hexagons:
            hexagon.update()

        for item in objects:
            item.render(screen)

        # render.map_render(screen, hexagons)
        # render.character_render(screen, char_hexagons)

        pygame.display.flip()
        clock.tick(50)
    pygame.quit()


if __name__ == "__main__":
    main()