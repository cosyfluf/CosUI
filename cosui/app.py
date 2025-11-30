import pyglet
from .theme import Colors

class App:
    def __init__(self, title="CosUI App", width=800, height=600):
        self.window = pyglet.window.Window(width, height, caption=title)
        self.widgets = []
        
        # Events binden
        self.window.event(self.on_draw)
        self.window.event(self.on_mouse_motion)
        self.window.event(self.on_mouse_press)

    def add(self, widget):
        self.widgets.append(widget)

    def on_draw(self):
        self.window.clear()
        # Hintergrund füllen
        pyglet.gl.glClearColor(Colors.BACKGROUND[0]/255, Colors.BACKGROUND[1]/255, Colors.BACKGROUND[2]/255, 1)
        
        for widget in self.widgets:
            widget.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        for widget in self.widgets:
            widget.check_hover(x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        for widget in self.widgets:
            if widget.check_hover(x, y):
                if hasattr(widget, 'on_click') and widget.on_click:
                    widget.on_click()

    def run(self):
        pyglet.app.run()