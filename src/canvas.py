from kandinsky import *
from ion import *
from time import sleep

WIDTH = 320
HEIGHT = 222
T = 0.01


def invertColor(colour):
    return tuple(255 - value for value in colour)


def moveListen(key, vector, cursor):
    if keydown(key):
        cursor.move(vector)
        if not keydown(KEY_TOOLBOX): sleep(T)


class Cursor:
    def __init__(self):
        self.x = WIDTH //  2
        self.y = HEIGHT // 2
        self.circle = self.getCircleOutline()
        self.covering = [(255, 255, 255)] * 13  # keeps track of what the cursor is currently covering
        self._draw()

    def getCircleOutline(self):
        x, y = self.x, self.y
        cEdge = lambda y2: [(x-2, y2), (x+2, y2)]
        cCap = lambda y2: [(x-1, y2), (x, y2), (x+1, y2)]
        l = cCap(y+2)
        l.extend(cEdge(y+1))
        l.extend(cEdge(y))
        l.extend(cEdge(y-1))
        l.extend(cCap(y-2))
        return l

    def getCircle(self):
        x, y = self.x, self.y
        cEdge = lambda y2: [(x-2, y2), (x-1, y2), (x, y2), (x+1, y2), (x+2, y2)]
        cCap = lambda y2: [(x-1, y2), (x, y2), (x+1, y2)]
        l = cCap(y + 2)
        l.extend(cEdge(y + 1))
        l.extend(cEdge(y))
        l.extend(cEdge(y - 1))
        l.extend(cCap(y - 2))
        return l

    def _draw(self):
        self.circle = self.getCircleOutline()
        for i, position in enumerate(self.circle):
            x, y = position[0], position[1]
            colour = get_pixel(x, y)
            self.covering[i] = colour
            set_pixel(x, y, invertColor(colour))

    def _undraw(self):
        for position, colour in zip(self.circle, self.covering):
            set_pixel(position[0], position[1], colour)

    def move(self, vector):
        self._undraw()
        self.x += vector[0]
        self.y += vector[1]
        self._draw()

    def draw(self, colour):
        for position in self.getCircle():
            set_pixel(position[0], position[1], colour)
        self.covering = [colour] * 13


cursor = Cursor()
while True:
    moveListen(KEY_LEFT, (-1, 0), cursor)
    moveListen(KEY_RIGHT, (1, 0), cursor)
    moveListen(KEY_UP, (0, -1), cursor)
    moveListen(KEY_DOWN, (0, 1), cursor)
    if keydown(KEY_OK): cursor.draw((255, 0, 0))