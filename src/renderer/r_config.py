from math import sin, cos

cube = []
for i in range(8):
    i = str(bin(i))[2:]
    i = "0" * (3 - len(i)) + i
    point = (int(i[0]), int(i[1]), int(i[2]))
    point = tuple(x * 2 - 1 for x in point)
    cube.append(point)

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
OBJECT = rings
