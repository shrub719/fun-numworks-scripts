cube = []
for i in range(8):
    i = str(bin(i))[2:]
    i = "0" * (3 - len(i)) + i
    point = (int(i[0]), int(i[1]), int(i[2]))
    point = tuple(x * 2 - 1 for x in point)
    cube.append(point)

edges = [
    (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7)
]

faces = [
    ([0, 1, 2, 3], "black"),
    ([4, 5, 6, 7], "black"),
    ([0, 1, 4, 5], "black"),
    ([2, 3, 6, 7], "black"),
    ([0, 2, 4, 6], "black"),
    ([1, 3, 5, 7], "black")
]

OBJECT = cube   # list of points, as coordinates
FACES = faces   # list of faces, as indexes in POINTS

if __name__ == "__main__":
    print(OBJECT)
    print(FACES)
