from r_cuboid import OBJECT

from kandinsky import *
from ion import *
from math import sin, cos


X = 320 // 2
Y = 222 // 2
SPEED = 0.01
SCALE = 50


def matrix_mul(A, B):
    result = tuple(sum(a * b for a, b in zip(A_row, B)) for A_row in A)
    return result


def to_coords(point):
    x = X + SCALE * point[0]
    y = Y + SCALE * point[1]
    return round(x), round(y)


def draw_obj(obj):
    for point in obj:
        x, y = to_coords(point)
        fill_rect(x, y, 5, 5, "black")


def erase_obj(obj):
    for point in obj:
        x, y = to_coords(point)
        fill_rect(x, y, 5, 5, "white")


def rotate(obj, angle, axis):
    c = cos(angle)
    s = sin(angle)
    if axis == 0:   # x
        rotation = [
            (1, 0, 0),
            (0, c, -s),
            (0, s, c)
        ]
    elif axis == 1: # z
        rotation = [
            (c, 0, s),
            (0, 1, 0),
            (-s, 0, c)
        ]
    else:
        rotation = [
            (c, -s, 0),
            (s, c, 0),
            (0, 0, 1)
        ]

    return [matrix_mul(rotation, point) for point in obj]


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


def get_rotation(obj):
    global SCALE
    keys = get_keys()
    if sum(keys):
        erase_obj(obj)
    if keys[0]:
        obj = rotate(obj, -SPEED, 0)
    if keys[1]:
        obj = rotate(obj, SPEED, 0)
    if keys[2]:
        obj = rotate(obj, -SPEED, 1)
    if keys[3]:
        obj = rotate(obj, SPEED, 1)
    if keys[4]:
        obj = rotate(obj, -SPEED, 2)
    if keys[5]:
        obj = rotate(obj, SPEED, 2)
    if keys[6]:
        SCALE -= 1
    if keys[7]:
        SCALE += 1

    return obj


while True:
    draw_obj(OBJECT)
    OBJECT = get_rotation(OBJECT)
