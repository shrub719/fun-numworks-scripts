from kandinsky import *
from ion import *
from time import sleep

WIDTH = 320
HEIGHT = 222
T = 0.005
SLOW = 0.02  # TODO: slowness toggle


def invertColour(colour):
    return tuple(255 - value for value in colour)


class Cursor:
    def __init__(self):
        self.x = WIDTH //  2
        self.y = HEIGHT // 2
        self.circle = self.getOutline()
        self.covering = [(255, 255, 255)] * 13  # keeps track of what the cursor is currently covering
        self._draw()
        # FIXME: one pixel showing up at start

    def getOutline(self):
        x, y = self.x, self.y
        cEdge = lambda y2: [(x-2, y2), (x+2, y2)]
        cCap = lambda y2: [(x-1, y2), (x, y2), (x+1, y2)]
        l = cCap(y+2)
        l.extend(cEdge(y+1))
        l.extend(cEdge(y))
        l.extend(cEdge(y-1))
        l.extend(cCap(y-2))
        return l

    def getFill(self):
        x, y = self.x, self.y
        row = lambda y2: [(x-1, y2), (x, y2), (x+1, y2)]
        l = row(y+1)
        l.extend(row(y))
        l.extend(row(y-1))
        return l

    def _draw(self):
        self.circle = self.getOutline()
        for i, position in enumerate(self.circle):
            x, y = position[0], position[1]
            colour = get_pixel(x, y)
            self.covering[i] = colour
            set_pixel(x, y, invertColour(colour))

    def _undraw(self):
        for position, colour in zip(self.circle, self.covering):
            set_pixel(position[0], position[1], colour)

    def move(self, vector):
        self._undraw()
        self.x += vector[0]
        self.y += vector[1]
        if self.x < 0: self.x = 0
        if self.y < 0: self.y = 0
        if self.x > WIDTH: self.x = WIDTH
        if self.y > HEIGHT: self.y = HEIGHT
        self._draw()

    def draw(self, colour):
        for position in self.getFill():
            set_pixel(position[0], position[1], colour)
        self.covering = [colour] * 13


def moveListen(key, vector, cursor):
    if keydown(key):
        cursor.move(vector)
        if not keydown(KEY_TOOLBOX): sleep(T)
        if keydown(KEY_BACKSPACE): sleep(SLOW)


cursor = Cursor()
colour = "black"
while True:
    moveListen(KEY_LEFT, (-1, 0), cursor)
    moveListen(KEY_RIGHT, (1, 0), cursor)
    moveListen(KEY_UP, (0, -1), cursor)
    moveListen(KEY_DOWN, (0, 1), cursor)
    if keydown(KEY_OK): cursor.draw(colour)
    if keydown(KEY_ONE): colour = "black"
    if keydown(KEY_TWO): colour = "white"
    if keydown(KEY_THREE): colour = "#ffb734"
    if keydown(KEY_FOUR): colour = "red"
    if keydown(KEY_FIVE): colour = "green"
    if keydown(KEY_SIX): colour = "blue"