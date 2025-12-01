import pygame
import sys
from .theme import Colors
from .utils import hex_to_rgb

class App:
    def __init__(self, title="CosUI App", width=800, height=600):
        # Initialize the rendering engine
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        
        self.width = width
        self.height = height
        self.widgets = []
        self.running = False
        self.clock = pygame.time.Clock()

    def add(self, widget):
        self.widgets.append(widget)

    def run(self):
        self.running = True
        
        while self.running:
            # 1. Event Handling
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                
                # Handle mouse motion for hover effects
                if event.type == pygame.MOUSEMOTION:
                    mouse_x, mouse_y = event.pos
                    for widget in self.widgets:
                        widget.check_hover(mouse_x, mouse_y)

                # Handle mouse clicks
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = event.pos
                    # Unfocus everything first
                    for widget in self.widgets:
                        widget.focused = False
                        
                    for widget in self.widgets:
                        if widget.check_hover(mouse_x, mouse_y):
                            if hasattr(widget, 'on_click') and widget.on_click:
                                widget.on_click()

                # Handle Keyboard Input
                if event.type == pygame.KEYDOWN:
                    for widget in self.widgets:
                        widget.handle_event(event)

            # 2. Drawing
            # Clear screen with background color
            self.screen.fill(hex_to_rgb(Colors.BACKGROUND))
            
            # Draw all widgets
            for widget in self.widgets:
                widget.draw(self.screen)

            # 3. Update Display
            pygame.display.flip()
            
            # Limit framerate to 60 FPS
            self.clock.tick(60)

        pygame.quit()
        sys.exit()