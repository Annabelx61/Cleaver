import pygame
from dataclasses import dataclass

class InputBox(pygame.Rect):
    """I'm sure there's a better way to do this. But creating my own 'Rect' class so that
    I can add my own methods the pygame.Rect class."""

    color_inactive: tuple[int, int, int] = (150, 150, 150)
    color_active: tuple[int, int, int] = (150, 150, 225)
    active: bool = False
    text: str = ''
    font: pygame.font.Font | None = None

    def activate(self):
        if not self.active:
            self.active = True
        else:
            self.active = False

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self, 2)
        render_text(screen, self.font, self.text, (self.x + 5, self.y + 5))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: # I RECOGNIZE THIS IS DOUBLE-CHECKED BUT ITS 2 AM
            if self.collidepoint(event.pos):  # Checks if event click was on InputBox
                if not self.active:  # If yes, flips the InputBox.active boolean if not active
                    self.activate()
            elif self.active:  # If no, deactivates it
                self.activate()
        elif event.type == pygame.KEYDOWN: # I RECOGNIZE THIS IS DOUBLE-CHECKED BUT ITS 2 AM
            if self.active:  # Makes sure the InputBox has been selected
                if event.key == pygame.K_RETURN:  # Key loop + string manipulation
                    self.activate()
                    text = self.text
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
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


    def render(self):
        x, y = self.position
        w, h = self.dimension

        button_text = Text(self.screen, int(h), self.message, x, y)

        while button_text.width > int(self.dimension[0]):
            self.dimension = (button_text.width + h, self.dimension[1])

        # Loop to add margins to the edges of the box and the text
        while int(self.dimension[0] - button_text.width) < h:
            self.dimension = (self.dimension[0] + 1, self.dimension[1])

        # ITS LATE and i cannot think of a better solution. If I try to add
        # height margins, it becomes a recursive issue since the dimension
        # is called at the start of the function. I could probably break
        # this function up and make it way better, but that's a later task.
        #
        # This little bit just creates a new set of dimensions with margins
        # that do NOT recursively cause the button to grow infinitely.
        if int(self.dimension[0] - button_text.width) == h:
            x_margin = h
        else:
            x_margin = self.dimension[0] - button_text.width
        y_margin = 0.2 * h
        adjusted_dimension = (self.dimension[0], self.dimension[1] + y_margin)

        button_fill = pygame.Rect(self.position, adjusted_dimension)
        button_border = pygame.Rect(self.position, adjusted_dimension)

        pygame.draw.rect(self.screen, self.color, button_fill, 0)
        pygame.draw.rect(self.screen, self.border_color, button_border, 2)

        button_pos = (x + 0.5 * x_margin,
                      y + 0.2 * y_margin)
        button_text.render(button_pos)

    # WIP
    def handle_event(self, event):
        x = 1


    @property
    def color(self):
        return self.color_active if self.active else self.color_inactive

    @property
    def center(self):
        center = (0.5 * self.dimension[0], 0.5 * self.dimension[1])
        return center

    @property
    def border_color(self):
        color = (0, 0, 0)
        return color

    @property
    def position(self) -> tuple[float, float]:

        position = (self.x_offset - 0.5 * self.dimension[0],
                    self.y_offset - 0.5 * self.dimension[1])

        return position


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
    info = pygame.display.Info() # finding window width/height; stolen from Anna
    screen_height = info.current_h
    screen_width = info.current_w

    title_text = "Cleaver the Pit"
    subtitle_text = "Wilson Chenault & Annabel Mehari"
    version1_text = "October 17 2026"
    version2_text = "Alpha Version 0.1.2"
    play_button = "Play"
    settings_button = "Settings"

    objects = [
        Button(screen, (200, 40), screen_width * 0.5, screen_height * 0.5,
               message = play_button),
        Button(screen, (200, 40), screen_width * 0.5, screen_height * 0.57,
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
    box = InputBox(vertices)

    return box