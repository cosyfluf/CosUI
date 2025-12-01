class Widget:
    def __init__(self, x=0, y=0, w=100, h=50):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.hovered = False
        self.focused = False  # New: Tracks if the widget is selected (e.g. for typing)

    def check_hover(self, mouse_x, mouse_y):
        """
        Checks if the mouse is inside the widget's boundaries.
        """
        self.hovered = (self.x < mouse_x < self.x + self.width and 
                        self.y < mouse_y < self.y + self.height)
        return self.hovered

    def handle_event(self, event):
        """
        Handle specific events like key presses.
        To be overridden by subclasses.
        """
        pass

    def draw(self, surface):
        """
        Draw command using the provided surface.
        To be overridden.
        """
        pass