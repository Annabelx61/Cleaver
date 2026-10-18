import pygame
import render, gui


def main():
    """Main function."""
    pygame.init()
    screen, hexagons, char_hexagons, clock, num_in_direction = render.initialize()

    terminated = False
    game_started = False
    texts, objects = gui.main_menu(screen)

    #debug = gui.Text(screen, 48)
    #texts.append(debug)

    while not terminated:

        screen.fill((255, 255, 255))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminated = True

            elif event.type == pygame.VIDEORESIZE:
                screen, hexagons, char_hexagons = render.resize(screen, event, num_in_direction)
            
            elif not game_started:
                for item in objects:
                    clicked = item.handle_event(event)
                    if clicked and item.message == "Play":
                        game_started = True

                # pos = pygame.mouse.get_pos()
                # debug.message = str(pos)
                # debug.x_offset, debug.y_offset = pos

        if game_started:
            for hexagon in hexagons:
                hexagon.update()

            render.map_render(screen, hexagons)
            render.character_render(screen, char_hexagons)
            
        else:
            for text in texts:
                text.render(text.position)

            for item in objects:
                item.render()

        pygame.display.flip()
        clock.tick(50)

    pygame.quit()


if __name__ == "__main__":
    main()