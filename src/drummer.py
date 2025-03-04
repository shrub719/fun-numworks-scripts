from kandinsky import *
from ion import *

COLOURS = [
    [(255, 50, 50), (50, 255, 50), (50, 50, 255)],
    [(255, 255, 50), (50, 255, 255), (255, 50, 255)],
]
KEYS = [
    [KEY_SEVEN, KEY_EIGHT, KEY_NINE],
    [KEY_FOUR, KEY_FIVE, KEY_SIX],
    [KEY_ONE, KEY_TWO, KEY_THREE]
]
FADE_SPEED = 5
HEIGHT = 74
WIDTH = 107
c_preset = 0


def multiply(vector, scalar):
    return (element * scalar for element in vector)


def getColour(value, i, j):
    pos = (j + i) % 3
    c = COLOURS[c_preset][pos]
    c = multiply(c, value / 100)
    return color(tuple(c))


def getInput(grid):
    for i in range(3):
        for j in range(3):
            if keydown(KEYS[i][j]):
                grid[i][j] = 100
    return grid


def draw(grid):
    top = 0
    for i, row in enumerate(grid):
        left = 0
        for j, cell in enumerate(row):
            c = getColour(cell, i, j)
            fill_rect(left, top, WIDTH, HEIGHT, c)
            left += WIDTH
        top += HEIGHT


def tick(grid):
    for i in range(3):
        for j in range(3):
            if grid[i][j] > 0:
                grid[i][j] = grid[i][j] - FADE_SPEED
            elif grid[i][j] < 0:
                grid[i][j] = 0
    return grid


def main():
    global c_preset
    grid = [[0, 0, 0] for i in range(3)]
    while True:
        grid = getInput(grid)
        draw(grid)
        grid = tick(grid)

        if keydown(KEY_DOT):
            c_preset += 1
            if c_preset >= len(COLOURS): c_preset = 0
            while keydown(KEY_DOT):
                pass


main()
