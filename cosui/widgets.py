import pygame
from .core import Widget
from .theme import Colors, Style
from .utils import hex_to_rgb

class Panel(Widget):
    def __init__(self, x, y, w, h, color=Colors.BACKGROUND):
        super().__init__(x, y, w, h)
        self.color = color

    def draw(self, surface):
        # Draw a simple rectangle
        pygame.draw.rect(
            surface, 
            hex_to_rgb(self.color), 
            (self.x, self.y, self.width, self.height)
        )

class Label(Widget):
    def __init__(self, text, x, y, size=Style.FONT_SIZE, color=Colors.TEXT):
        super().__init__(x, y, 0, 0)
        self.text = text
        self.size = size
        self.color = color
        # Font caching could be improved here
        self.font = pygame.font.SysFont(Style.FONT_NAME, self.size)

    def draw(self, surface):
        # Render text to a temporary surface
        text_surf = self.font.render(self.text, True, hex_to_rgb(self.color))
        surface.blit(text_surf, (self.x, self.y))

class Button(Widget):
    def __init__(self, text="Button", x=100, y=100, w=160, h=40, on_click=None):
        super().__init__(x, y, w, h)
        self.text = text
        self.on_click = on_click
        self.font = pygame.font.SysFont(Style.FONT_NAME, 14)

    def draw(self, surface):
        # Determine color based on hover state
        color_hex = Colors.HOVER if self.hovered else Colors.PRIMARY
        color_rgb = hex_to_rgb(color_hex)
        
        # Draw rounded rectangle (border_radius applies rounding)
        rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, color_rgb, rect, border_radius=Style.ROUNDING)
        
        # Draw centered text
        text_surf = self.font.render(self.text, True, hex_to_rgb(Colors.BUTTON_TEXT))
        text_rect = text_surf.get_rect(center=(self.x + self.width//2, self.y + self.height//2))
        surface.blit(text_surf, text_rect)

class Input(Widget):
    def __init__(self, x=100, y=200, w=200, h=40):
        super().__init__(x, y, w, h)
        self.text = ""
        self.font = pygame.font.SysFont(Style.FONT_NAME, 14)
        
    def on_click(self):
        self.focused = True

    def handle_event(self, event):
        # Handle typing only if focused
        if self.focused and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            else:
                self.text += event.unicode

    def draw(self, surface):
        # Colors
        bg_color = hex_to_rgb(Colors.INPUT_BG)
        border_color = hex_to_rgb(Colors.INPUT_BORDER if self.focused else Colors.TEXT)
        text_color = hex_to_rgb(Colors.TEXT)

        # Draw Background (Rounded)
        rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(surface, bg_color, rect, border_radius=Style.ROUNDING)
        
        # Draw Border (Rounded) - width=2 implies outline
        pygame.draw.rect(surface, border_color, rect, width=2, border_radius=Style.ROUNDING)

        # Draw Text inside
        text_surf = self.font.render(self.text, True, text_color)
        # Add a little padding for the text
        surface.blit(text_surf, (self.x + 10, self.y + (self.height - text_surf.get_height()) // 2))