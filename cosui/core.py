class Widget:
    def __init__(self, x=0, y=0, w=100, h=50):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.hovered = False

    def check_hover(self, mouse_x, mouse_y):
        # Einfache Kollisionsabfrage
        self.hovered = (self.x < mouse_x < self.x + self.width and 
                        self.y < mouse_y < self.y + self.height)
        return self.hovered

    def draw(self):
        pass # Muss überschrieben werden