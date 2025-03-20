from kandinsky import *
from ion import *

WIDTH = 320
HEIGHT = 222

class Cursor:
    def __init__(self):
        self.x = WIDTH //  2
        self.y = HEIGHT // 2
        self.under = color(255, 255, 255)  # keeps track of what the cursor is currently covering

    def setColor(self):
