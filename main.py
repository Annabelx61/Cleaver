import pygame
import render, gui


def main():
    """Main function."""
    pygame.init()
    screen, hexagons, char_hexagons, clock, num_in_direction = render.initialize()
    terminated = False

    debug = gui.Text(screen, 48)
    texts, objects = gui.main_menu(screen)
    texts.append(debug)
    while not terminated:
        screen.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminated = True
            elif event.type == pygame.VIDEORESIZE:
                screen, hexagons, char_hexagons = render.resize(screen, event, num_in_direction)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                debug.message = str(pos)
                debug.x_offset, debug.y_offset = pos

            # for item in objects:
            #     item.handle_event(event)


        for hexagon in hexagons:
            hexagon.update()

        for text in texts:
            text.render(text.position)

        for item in objects:
            item.render()

        # render.map_render(screen, hexagons)
        # render.character_render(screen, char_hexagons)

        pygame.display.flip()
        clock.tick(50)
    pygame.quit()


if __name__ == "__main__":
    main()