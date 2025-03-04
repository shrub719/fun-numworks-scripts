from kandinsky import *
from ion import *

COLOURS = [
    ["black"] * 5 + ["white"],
    ["#ffadad", "#ffd6a5", "#fdffb6", "#caffbf", "#a0c4ff", "white"],
    ["#5BCEFA", "#F5A9B8", "#5BCEFA", "#F5A9B8", "#5BCEFA", "white"],
    ["white"] * 5 + ["black"],
]
KEYS = [KEY_SEVEN, KEY_EIGHT, KEY_NINE, KEY_LEFTPARENTHESIS, KEY_RIGHTPARENTHESIS]
HEIGHT = 8
c_preset = 0


def k(key):
    if keydown(key):
        return 1
    return 0


def getInput():
    r = []
    for key in KEYS:
        r.append(k(key))
    return r


def draw(rows):
    top = 0
    for row in rows:
        left = 0
        for i, key in enumerate(row):
            c = COLOURS[c_preset][-1]
            if key: c = COLOURS[c_preset][i]
            fill_rect(left, top, 64, HEIGHT, c)
            left += 64
        top += HEIGHT


def main():
    global c_preset
    rows = [[0, 0, 0, 0, 0] for i in range(222 // HEIGHT)]
    while True:
        rows.pop(0)
        rows.append(getInput())
        draw(rows)

        if keydown(KEY_EXE):
            c_preset += 1
            if c_preset >= len(COLOURS): c_preset = 0
            while keydown(KEY_EXE):
                pass


main()
