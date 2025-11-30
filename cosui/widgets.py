import pyglet
from .core import Widget
from .theme import Colors, Style

class Panel(Widget):
    def __init__(self, x, y, w, h, color=Colors.BACKGROUND):
        super().__init__(x, y, w, h)
        self.color = color

    def draw(self):
        pyglet.shapes.Rectangle(
            self.x, self.y, self.width, self.height, 
            color=self.color[:3]
        ).draw()

class Label(Widget):
    def __init__(self, text, x, y, size=16, color=Colors.TEXT):
        super().__init__(x, y, 0, 0) # Größe ist hier zweitrangig
        self.text = text
        self.size = size
        self.color = color

    def draw(self):
        pyglet.text.Label(
            self.text, font_name=Style.FONT, font_size=self.size,
            x=self.x, y=self.y, color=(*self.color, 255)
        ).draw()

class Button(Widget):
    def __init__(self, text="Button", x=100, y=100, w=160, h=40, on_click=None):
        super().__init__(x, y, w, h)
        self.text = text
        self.on_click = on_click

    def draw(self):
        # Hover Effekt
        color = Colors.HOVER if self.hovered else Colors.PRIMARY
        
        # Button Hintergrund
        pyglet.shapes.Rectangle(
            self.x, self.y, self.width, self.height, 
            color=color[:3]
        ).draw()
        
        # Button Text (Zentriert)
        pyglet.text.Label(
            self.text, font_name=Style.FONT, font_size=14,
            x=self.x + self.width//2, y=self.y + self.height//2,
            anchor_x='center', anchor_y='center', color=(255,255,255,255)
        ).draw()