from math import sin, cos
import numpy as np  # TODO: add to requirements.txt

O_cube = np.empty((0, 3))
for a in [-1, 1]:
    for b in [-1, 1]:
        c = -1
        for i in range(5):
            O_cube = np.append(O_cube, [[a, b, c]], axis=0)
            O_cube = np.append(O_cube, [[a, c, b]], axis=0)
            O_cube = np.append(O_cube, [[c, a, b]], axis=0)
            c += 0.5

O_cuboid = None # TODO: vectorise or whatever

O_rings = np.concatenate(
    (
        [(sin(t*0.2), cos(t*0.2), 0) for t in range(31)],
        [(0, sin(t*0.2), cos(t*0.2)) for t in range(31)]
    ),
    axis=0
)


O_rings2 = np.concatenate(
    (
        [(sin(t*0.4), cos(t*0.4), 0) for t in range(16)],
        [(0, sin(t*0.4), cos(t*0.4)) for t in range(16)],
        [(sin(t*0.4), 0, cos(t*0.4)) for t in range(16)]
    ),
    axis=0
)

O_donut = np.concatenate(
    (
        [(sin(t*0.2), cos(t*0.2), 0.2) for t in range(31)],
        [(sin(t*0.2), cos(t*0.2), -0.2) for t in range(31)]
    ),
    axis=0
)


C_grey = (0.8, 0.8, 0.8)
C_orange = (1, 0.7, 0.2)
C_purple = (0.5, 0.2, 1)


if __name__ == "__main__":
    print("CUBE", O_cube)
    print("CUBOID", O_cuboid)
    print("RINGS", O_rings)
    print("RINGS2", O_rings2)
    print("DONUT", O_donut)


# ===== CONFIG =====

# rotation
IN_PLACE = True
SPEED = 0.02

# options: grey / orange / purple
COLOUR = C_purple

# options: cube / cuboid / rings / rings2 / donut
OBJECT = O_donut
