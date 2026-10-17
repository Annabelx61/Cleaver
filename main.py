import pygame
import render, gui


def main():
    """Main function."""
    pygame.init()
    screen, hexagons, char_hexagons, clock, num_in_direction = render.initialize()
    gui.play(screen, hexagons, clock, num_in_direction)
    pygame.quit()


if __name__ == "__main__":
    main()