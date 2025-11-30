import pyglet
from .core import Widget
from .theme import Colors, Style

class Button(Widget):
    def __init__(self, text="Button", x=100, y=100, on_click=None):
        super().__init__(x, y, 160, 50)
        self.text = text
        self.on_click = on_click
        self.batch = pyglet.graphics.Batch()

    def draw(self):
        # Farbe ändern wenn Maus drauf ist (Reaktivität)
        color = Colors.HOVER if self.hovered else Colors.PRIMARY
        
        # Rechteck zeichnen (Modernisierung: Runde Ecken simulieren wir hier simpel)
        pyglet.shapes.Rectangle(
            self.x, self.y, self.width, self.height, 
            color=color[:3]
        ).draw()
        
        # Text rendern
        label = pyglet.text.Label(
            self.text, font_name=Style.FONT, font_size=14,
            x=self.x + self.width//2, y=self.y + self.height//2,
            anchor_x='center', anchor_y='center', color=(255,255,255,255)
        )
        label.draw()