from kandinsky import *
from ion import *
from math import sin, cos
from r_config import OBJECT, IN_PLACE, SPEED, COLOUR


X = 320 // 2
Y = 222 // 2


def matrix_mul(A, B):
    result = [tuple(sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)) for A_row in A]
    return result


def rotate_point(rotation, coordinate):
    result = tuple(sum(a * b for a, b in zip(row, coordinate)) for row in rotation)
    return result


def to_coords(point, scale):
    x = X + scale * point[0]
    y = Y + scale * point[1]
    c = (point[2] + 3) / 5 * 255
    return round(x), round(y), (COLOUR[0]*c, COLOUR[1]*c, COLOUR[2]*c)


def draw_obj(obj, scale, size):
    s = size // 2
    coords = [to_coords(point, scale) for point in obj]
    for point in coords:
        x, y, c = point
        fill_rect(x-s, y-s, size, size, c)


def erase_obj(obj, scale, size):
    s = size // 2
    coords = [to_coords(point, scale) for point in obj]
    for point in coords:
        x, y, c = point
        fill_rect(x-s, y-s, size, size, "white")


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


def get_input(x, y, z, scale, size, in_place=False):
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
    if keys[8]:
        size -= 1
    if keys[9]:
        size += 1

    return redraw, x, y, z, scale, size


x, y, z = 0, 0, 0
scale = 50
size = 5
obj = OBJECT

draw_obj(obj, scale, size)
while True:
    old_scale = scale
    old_size = size
    redraw, x, y, z, scale, size = get_input(x, y, z, scale, size, IN_PLACE)
    if redraw:
        erase_obj(obj, old_scale, old_size)
        obj = rotate(obj, x, y, z)
        draw_obj(obj, scale, size)
