import pygame

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
         # I RECOGNIZE THIS IS DOUBLE-CHECKED BUT ITS 2 AM ----- LMAOOO 
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if self.collidepoint(event.pos):  
                self.active()
        elif event.type == pygame.KEYDOWN and self.active: 
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key != pygame.K_RETURN:  
                self.text += event.unicode

def font_initialization(size: int = 24):
    font = pygame.font.SysFont("Times New Roman", size)
    return font

def render_text(screen, font, message, position):
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