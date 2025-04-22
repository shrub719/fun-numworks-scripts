from r_cube import OBJECT

from kandinsky import *
from ion import *
from math import sin, cos
from time import sleep


X = 320 // 2
Y = 222 // 2
SPEED = 0.01


def matrix_mul(A, B):
    result = [tuple(sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)) for A_row in A]
    return result


def rotate_point(rotation, coordinate):
    result = tuple(sum(a * b for a, b in zip(row, coordinate)) for row in rotation)
    return result


def to_coords(point):
    x = X + SCALE * point[0]
    y = Y + SCALE * point[1]
    return round(x), round(y)


def draw_obj(obj):
    coords = [to_coords(point) for point in obj]
    for point in coords:
        x, y = point
        fill_rect(x, y, 5, 5, "black")


def rotate(obj, x, y, z):
    rotation = [
        (1, 0, 0),
        (0, 1, 0),
        (0, 0, 1)
    ]
    if x != 0:
        s, c = sin(x), cos(x)
        r = [
            (1, 0, 0),
            (0, c, -s),
            (0, s, c)
        ]
        rotation = matrix_mul(r, rotation)
    if y != 0:
        s, c = sin(y), cos(y)
        r = [
            (c, 0, s),
            (0, 1, 0),
            (-s, 0, c)
        ]
        rotation = matrix_mul(r, rotation)
    if z != 0:
        s, c = sin(z), cos(z)
        r = [
            (c, -s, 0),
            (s, c, 0),
            (0, 0, 1)
        ]
        rotation = matrix_mul(r, rotation)

    return [rotate_point(rotation, point) for point in obj]


def get_keys():
    return [
        keydown(KEY_DOWN),
        keydown(KEY_UP),
        keydown(KEY_LEFT),
        keydown(KEY_RIGHT),
        keydown(KEY_SHIFT),
        keydown(KEY_ALPHA),
        keydown(KEY_MINUS),
        keydown(KEY_PLUS)
    ]


def get_input(x, y, z, scale):
    keys = get_keys()

    redraw = sum(keys)

    if keys[0]:
        x -= SPEED
    if keys[1]:
        x += SPEED
    if keys[2]:
        y -= SPEED
    if keys[3]:
        y += SPEED
    if keys[4]:
        z -= SPEED
    if keys[5]:
        z += SPEED
    if keys[6]:
        scale -= 1
    if keys[7]:
        scale += 1

    return redraw, x, y, z, scale


def get_rotation(obj):
    global SCALE, x, y, z
    keys = get_keys()
    redraw = sum(keys)

    if redraw:
        draw_obj()

    if keys[0]:
        x -= SPEED
    if keys[1]:
        x += SPEED
    if keys[2]:
        y -= SPEED
    if keys[3]:
        y += SPEED
    if keys[4]:
        z -= SPEED
    if keys[5]:
        z += SPEED
    if keys[6]:
        SCALE -= 1
    if keys[7]:
        SCALE += 1

    obj = rotate(obj, x, y, z)
    if redraw:
        draw_obj(obj)

    return obj


x, y, z = 0, 0, 0
scale = 50
draw_obj(OBJECT)
while True:
    redraw, x, y, z, scale = get_input(x, y, z, scale)
    get_rotation(OBJECT)
