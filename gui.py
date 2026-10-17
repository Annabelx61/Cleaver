import pygame

class InputBox(pygame.Rect):
    """I'm sure there's a better way to do this. But creating my own 'Rect' class so that
    I can add my own methods the pygame.Rect class."""

    color_inactive: tuple[int, int, int] = (150, 150, 150)
    color_active: tuple[int, int, int] = (150, 150, 225)
    active: bool = False
    text: str = ''
    font: pygame.font.Font | None = None

    color: color_active if active else color_inactive

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





def font_initialization(size: int = 24):
    font = pygame.font.SysFont("Times New Roman", size)
    return font

def render_text(screen, font, message: str, position: tuple[float, float]):
    if font is None:
        font = font_initialization()

    text = font.render(message, False, (0, 0, 0))
    screen.blit(text, position)

def main_menu(screen) -> list:
    screen.fill((255, 255, 255))

    title_font = font_initialization(72)
    box_font = font_initialization(48)
    title = "Cleaver the Pit"

    box = input_box(screen, box_font, (200, 200, 400, 32))
    render_text(screen, title_font, title, (0, 0))

    return [box]

def input_box(screen, font, vertices: tuple[float, ...]) -> pygame.Rect:
    """Renders input box -- lots of AI generated test code..."""
    box = InputBox(vertices)

    # render_text(screen, font, text, (box.x + 5, box.y + 5))
    # pygame.draw.rect(screen, color, box, 2)

    return box