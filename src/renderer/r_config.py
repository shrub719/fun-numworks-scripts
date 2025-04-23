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

rings = [(sin(t*0.2), cos(t*0.2), 0) for t in range(31)] + [(0, cos(t*0.2), sin(t*0.2)) for t in range(31)]

pyramid = [
    (-1, -1, -1), 
    (-1, -1, 1),
    (1, -1, -1),
    (1, -1, 1),
    (0, 1.4, 0)
]


# ===== CONFIG =====

# rotation
IN_PLACE = True
SPEED = 0.02

# options: cube / cuboid / rings / pyramid
OBJECT = cube
