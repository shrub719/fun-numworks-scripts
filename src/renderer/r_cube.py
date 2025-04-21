cube = []
for i in range(8):
    i = str(bin(i))[2:]
    i = "0" * (3 - len(i)) + i
    point = (int(i[0]), int(i[1]), int(i[2]))
    point = tuple(x * 2 - 1 for x in point)
    cube.append(point)

OBJECT = cube
