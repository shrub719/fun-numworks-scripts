from kandinsky import *
from ion import *

def draw(colour):
    fill_rect(0, 0, 320, 200, color(tuple(colour)))

def show(colour):
    draw_string(str(colour[0]), 0, 200)
    draw_string(str(colour[1]), 50, 200)
    draw_string(str(colour[2]), 100, 200)

def listen(key, colour, value, changeBy):
    if keydown(key):
        colour[value] += changeBy
        if colour[value] > 255:
            colour[value] = 255
        elif colour[value] < 0:
            colour[value] = 0
        draw(colour)

colour = [0, 0, 0]
draw(colour)
while not keydown(KEY_BACK):
    listen(KEY_FOUR, colour, 0, 1)
    listen(KEY_FIVE, colour, 1, 1)
    listen(KEY_SIX, colour, 2, 1)
    listen(KEY_ONE, colour, 0, -1)
    listen(KEY_TWO, colour, 1, -1)
    listen(KEY_THREE, colour, 2, -1)
    show(colour)

print(*colour)