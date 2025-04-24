from math import sin, cos

O_cube = []
for a in [-1, 1]:
    for b in [-1, 1]:
        c = -1
        for i in range(5):
            O_cube.append((a, b, c))
            O_cube.append((a, c, b))
            O_cube.append((c, a, b))
            c += 0.5

O_cuboid = [(point[0] * 2, point[1], point[2]) for point in O_cube]

O_rings = [(sin(t*0.2), cos(t*0.2), 0) for t in range(31)] + [(0, sin(t*0.2), cos(t*0.2)) for t in range(31)]
O_rings2 = [(sin(t*0.4), cos(t*0.4), 0) for t in range(16)] + [(0, sin(t*0.4), cos(t*0.4)) for t in range(16)] + [(sin(t*0.4), 0, cos(t*0.4)) for t in range(16)]
O_donut = [(sin(t*0.2), cos(t*0.2), 0) for t in range(31)]
O_donut = O_donut + [(x, y, z+0.3) for x, y, z in O_donut]

O_pyramid = [
    (-1, -1, -1), 
    (-1, -1, 1),
    (1, -1, -1),
    (1, -1, 1),
    (0, 1.4, 0)
]


C_grey = (0.8, 0.8, 0.8)
C_orange = (1, 0.7, 0.2)
C_purple = (0.5, 0.2, 1)


# ===== CONFIG =====

# rotation
IN_PLACE = True
SPEED = 0.02

# options: grey / orange / purple
COLOUR = C_purple

# options: cube / cuboid / rings / rings2 / donut
OBJECT = O_donut
