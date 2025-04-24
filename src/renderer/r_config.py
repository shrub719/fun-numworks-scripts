from math import sin, cos

cube = []
for a in [-1, 1]:
    for b in [-1, 1]:
        c = -1
        for i in range(5):
            cube.append((a, b, c))
            cube.append((a, c, b))
            cube.append((c, a, b))
            c += 0.5


cuboid = [(point[0] * 2, point[1], point[2]) for point in cube]

rings = [(sin(t*0.2), cos(t*0.2), 0) for t in range(31)] + [(0, sin(t*0.2), cos(t*0.2)) for t in range(31)]
rings2 = [(sin(t*0.4), cos(t*0.4), 0) for t in range(16)] + [(0, sin(t*0.4), cos(t*0.4)) for t in range(16)] + [(sin(t*0.4), 0, cos(t*0.4)) for t in range(16)]

pyramid = [
    (-1, -1, -1), 
    (-1, -1, 1),
    (1, -1, -1),
    (1, -1, 1),
    (0, 1.4, 0)
]

grey = (0.8, 0.8, 0.8)   # TODO: TEST
orange = (1, 0.7, 0.2)


# ===== CONFIG =====

# rotation
IN_PLACE = True
SPEED = 0.02

# options: grey / orange
COLOUR = grey

# options: cube / cuboid / rings / rings2
OBJECT = cube
