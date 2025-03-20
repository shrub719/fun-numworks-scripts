from kandinsky import *
from ion import *
from time import sleep

WIDTH = 320
HEIGHT = 222
SLOW = 0.01
FAST = 0.002
diff = SLOW - FAST


def invertColor(colour):
    return tuple(255 - value for value in colour)


def moveListen(key, vector, cursor):
    if keydown(key):
        cursor.move(vector)
        sleep(FAST)
        if not keydown(KEY_TOOLBOX): sleep(diff)


class Cursor:
    def __init__(self):
        self.x = WIDTH //  2
        self.y = HEIGHT // 2
        self.covering = (255, 255, 255)  # keeps track of what the cursor is currently covering
        self._draw()

    def _draw(self):
        set_pixel(self.x, self.y, invertColor(self.covering))

    def _undraw(self):
        set_pixel(self.x, self.y, self.covering)

    def move(self, vector):
        self._undraw()
        self.x += vector[0]
        self.y += vector[1]
        self.covering = get_pixel(self.x, self.y)
        self._draw()

    def draw(self, colour):
        self.covering = colour


cursor = Cursor()
while True:
    moveListen(KEY_LEFT, (-1, 0), cursor)
    moveListen(KEY_RIGHT, (1, 0), cursor)
    moveListen(KEY_UP, (0, -1), cursor)
    moveListen(KEY_DOWN, (0, 1), cursor)
    if keydown(KEY_OK): cursor.draw((255, 0, 0))