from kandinsky import *
from ion import *
from math import sin, cos
from r_config import OBJECT, IN_PLACE


X = 320 // 2
Y = 222 // 2
SPEED = 0.02


def matrix_mul(A, B):
    result = [tuple(sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)) for A_row in A]
    return result


def rotate_point(rotation, coordinate):
    result = tuple(sum(a * b for a, b in zip(row, coordinate)) for row in rotation)
    return result


def to_coords(point, scale):
    x = X + scale * point[0]
    y = Y + scale * point[1]
    c = 255 - (point[2] + 3) * 255 / 5
    return round(x), round(y), (c, c, c)


def draw_obj(obj, scale):
    coords = [to_coords(point, scale) for point in obj]
    for point in coords:
        x, y, c = point
        fill_rect(x, y, 5, 5, c)


def erase_obj(obj, scale):
    coords = [to_coords(point, scale) for point in obj]
    for point in coords:
        x, y, c = point
        fill_rect(x, y, 5, 5, "white")


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


def get_input(x, y, z, scale, in_place=False):
    keys = get_keys()

    redraw = sum(keys)

    if in_place:
        x, y, z = 0, 0, 0

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


x, y, z = 0, 0, 0
scale = 50
obj = OBJECT

draw_obj(obj, scale)
while True:
    old_scale = scale
    redraw, x, y, z, scale = get_input(x, y, z, scale, IN_PLACE)
    if redraw:
        if IN_PLACE:
            new_obj = rotate(obj, x, y, z)
        else:
            new_obj = rotate(OBJECT, x, y, z)
        erase_obj(obj, old_scale)
        obj = new_obj
        draw_obj(obj, scale)
