from kandinsky import *
from ion import *
from math import sin, cos

try:
    from r_config import OBJECT, SPEED, COLOUR
except ModuleNotFoundError:
    SPEED = 0.05
    COLOUR = (0.5, 0.2, 1)
    OBJECT = [(sin(t * 0.2), cos(t * 0.2), 0) for t in range(31)]
    OBJECT = OBJECT + [(x, y, z + 0.3) for x, y, z in OBJECT]


X = 320 // 2
Y = 222 // 2
S = sin(SPEED)
C = cos(SPEED)


def to_coords(point, scale):
    x = X + scale * point[0]
    y = Y + scale * point[1]
    c = (point[2] + 3) / 5 * 255
    return round(x), round(y), (COLOUR[0]*c, COLOUR[1]*c, COLOUR[2]*c)


def draw_obj(obj, scale, size):
    s = size // 2
    coords = [to_coords(point, scale) for point in obj]
    for x, y, c in coords:
        fill_rect(x-s, y-s, size, size, c)


def erase_obj():
    fill_rect(0, 0, 320, 222, "white")


def matrix_mul(A, B):
    result = [tuple(sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)) for A_row in A]
    return result


def rotate_point(rotation, coordinate):
    result = tuple(sum(a * b for a, b in zip(row, coordinate)) for row in rotation)
    return result


def rotate(obj, x, y, z):
    rotation = [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
    ]
    if x != 0:
        s, c = S, C
        if x < 0: s = -S

        r = [
            (1, 0, 0),
            (0, c, -s),
            (0, s, c)
        ]
        rotation = matrix_mul(r, rotation)
    if y != 0:
        s, c = S, C
        if y < 0: s = -S

        r = [
            (c, 0, s),
            (0, 1, 0),
            (-s, 0, c)
        ]
        rotation = matrix_mul(r, rotation)
    if z != 0:
        s, c = S, C
        if z < 0: s = -S

        r = [
            (c, -s, 0),
            (s, c, 0),
            (0, 0, 1)
        ]
        rotation = matrix_mul(r, rotation)

    # TODO: turn into for loop with insort
    return sorted((rotate_point(rotation, point) for point in obj), key = lambda point: point[2])


def get_keys():
    return [
        keydown(KEY_DOWN),
        keydown(KEY_UP),
        keydown(KEY_LEFT),
        keydown(KEY_RIGHT),
        keydown(KEY_SHIFT),
        keydown(KEY_ALPHA),
        keydown(KEY_MINUS),
        keydown(KEY_PLUS),
        keydown(KEY_DIVISION),
        keydown(KEY_MULTIPLICATION)
    ]


def get_input(scale, size):
    x, y, z = 0, 0, 0
    keys = get_keys()
    redraw = sum(keys)

    if redraw:
        if keys[0]:
            x = -1
        if keys[1]:
            x = 1
        if keys[2]:
            y = -1
        if keys[3]:
            y = 1
        if keys[4]:
            z = -1
        if keys[5]:
            z = 1
        if keys[6]:
            scale -= 1
        if keys[7]:
            scale += 1
        if keys[8]:
            size -= 1
        if keys[9]:
            size += 1

    return redraw, x, y, z, scale, size


scale = 50
size = 25
obj = OBJECT

draw_obj(obj, scale, size)
while True:
    old_scale = scale
    old_size = size
    redraw, x, y, z, scale, size = get_input(scale, size)
    if redraw:
        obj = rotate(obj, x, y, z)
        erase_obj()
        draw_obj(obj, scale, size)
