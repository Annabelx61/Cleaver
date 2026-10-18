import pygame
from dataclasses import dataclass

class InputBox(pygame.Rect):
    """ Constructor Method to initialize the rectangle"""
    def __init__(self, vertices, font):
        super().__init__(vertices)

        self.font = font
        self.text = ""
        self.active = False

        self.color_inactive = (150, 150, 150)
        self.color_active = (150, 150, 225)
        

    # Input Box is gray when inactive and blue-purple when active
    @property
    def color(self):
        if self.active:
            return self.color_active 
        else: 
            return self.color_inactive

    def activate(self):
        if not self.active:
            self.active = True
        else:
            self.active = False

    def render(self, screen):
        """ Draw the input box and its current text onto the screen. """
        pygame.draw.rect(screen, self.color, self, 2)
        text_surface = self.font.render(self.text, True, (0,0,0)) # calling render on self.font to turn it into a image like surface
        screen.blit(text_surface, (self.x + 5, self.y + 5)) # using screen.blitz(surface, position) to draw that surface on the screen

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if self.collidepoint(event.pos):  
                self.activate()
        elif event.type == pygame.KEYDOWN and self.active: 
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key != pygame.K_RETURN:  
                self.text += event.unicode

    @property
    def color(self):
        return self.color_active if self.active else self.color_inactive

@dataclass
class Text:
    """Class to easily handle text rendering
    WIP: Stuff to center in an existing rectangle (i.e. button)
       : More preset positions like centered and bottom_right"""

    screen: pygame.Surface
    font_size: int
    message: str = ''
    x_offset: float = 0
    y_offset: float = 0
    color: tuple[int, ...] = (0, 0, 0)

    centered: bool = False
    bottom_right: bool = False

    def render(self, position):
        self.screen.blit(self.surface, position)

    @property
    def surface(self):
        return self.font_init.render(self.message, True, self.color)

    @property
    def font_init(self):
        return pygame.font.SysFont("Times New Roman", self.font_size)

    @property
    def center(self):
        center = 0.5 * self.screen.get_width() - 0.5 * self.width
        return center

    @property
    def position(self) -> tuple[float, float]:

        if self.centered:
            position = (self.center, self.y_offset)
        elif self.bottom_right:
            position = (self.screen.get_width() + self.x_offset - self.width,
                        self.screen.get_height() + self.y_offset - self.height)
        else:
            position = (self.x_offset - 0.5 * self.width,
                        self.y_offset - 0.5 * self.height)

        return position

    @property
    def width(self):
        return self.surface.get_width()

    @property
    def height(self):
        return self.surface.get_height()

@dataclass
class Button:
    """Class to handle button rendering and functionality"""

    screen: pygame.Surface
    dimension: tuple[float, float]
    x_offset: float = 0
    y_offset: float = 0
    color_inactive: tuple[int, int, int] = (225, 225, 225)
    color_active: tuple[int, int, int] = (150, 150, 150)
    active: bool = False
    message: str = ''
    font: pygame.font.Font | None = None

    @property
    def position(self):
        x = self.x_offset - self.dimension[0] / 2
        y = self.y_offset - self.dimension[1] / 2
        return (x, y)

    @property
    def rect(self):
        # Using pygame.Rect to get the button top-left position, width and height
        return pygame.Rect(
            int(self.position[0]),
            int(self.position[1]),
            int(self.dimension[0]),
            int(self.dimension[1])
        )

    @property
    def color(self):
        return self.color_active if self.active else self.color_inactive

    @property
    def center(self):
        center = (0.5 * self.dimension[0], 0.5 * self.dimension[1])
        return center

    @property
    def border_color(self):
        return (0, 0, 0)

    def render(self):
        x, y = self.position
        w, h = self.dimension

        button_rect = pygame.Rect(x, y, w, h)

        # Draws the button based on its hover state (self.color or self.border_color)
        pygame.draw.rect(self.screen, self.color, button_rect)
        pygame.draw.rect(self.screen, self.border_color, button_rect, width = 2)

        # Center the text in the button
        font = pygame.font.SysFont("Times New Roman", int(h * 0.6))
        text = font.render(self.message, True, (0,0,0))
        # .get_rect() -> returns a pygame.Rect that matches the text size, thank you ai
        text_rect = text.get_rect(center = self.rect.center) 
        self.screen.blit(text, text_rect)

    def handle_event(self, event):
        # hightlight when the mouse moves on the button
        if event.type == pygame.MOUSEMOTION:
            self.active = self.rect.collidepoint(event.pos)

        # For now return True only when the button is clicked
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # event.button == 1 -> left click, 2 -> middle click, 3 -> right click
            if event.button == 1 and self.rect.collidepoint(event.pos):
                return True
        return False


def font_initialization(size: int = 24):
    font = pygame.font.SysFont("Times New Roman", size)
    return font

def render_text(screen, font, message: str, position: tuple[float, float], centered: bool = False):
    if font is None:
        font = font_initialization()
    text = font.render(message, False, (0, 0, 0))

    if centered:
        position = (position[0] - 0.5 * text.get_width(), position[1])
    screen.blit(text, position)

def main_menu(screen) -> tuple[list, list]:
    screen.fill((255, 255, 255))
    # oops I think we need to get the windows size instead of the monitor's size :p
    screen_height = screen.get_height()
    screen_width = screen.get_width()

    title_text = "Cleaver the Pit"
    subtitle_text = "Wilson Chenault & Annabel Mehari"
    version1_text = "October 17 2026"
    version2_text = "Alpha Version 0.1.2"
    play_button = "Play"
    settings_button = "Settings"

    objects = [
        Button(screen, (300, 80), screen_width * 0.5, screen_height * 0.48,
               message = play_button),
        Button(screen, (300, 80), screen_width * 0.5, screen_height * 0.60,
               message = settings_button)
    ]

    texts = [
        Text(screen, 72, title_text, y_offset = screen_height * 0.1, centered = True),
        Text(screen, 36, subtitle_text, y_offset = screen_height * 0.2, centered = True),
        Text(screen, 24, version1_text, y_offset = screen_height * -0.025, bottom_right = True),
        Text(screen, 24, version2_text, bottom_right = True)
    ]

    for text in texts:
        text.render(text.position)

    return texts, objects

def input_box(screen, font, vertices: tuple[float, ...]) -> InputBox:
    """Renders input box"""
    box = InputBox(vertices, font)

    return box