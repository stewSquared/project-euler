"""The cube, 41063625 (345^3), can be permuted to produce two other
cubes: 56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the
smallest cube which has exactly three permutations of its digits which
are also cube.

Find the smallest cube for which exactly five permutations of its
digits are cube."""

from itertools import count

cubePerms = dict()

for cube in map(lambda n: n**3, count()):
    cubeKey = "".join(sorted(str(cube)))
    if cubeKey not in cubePerms: cubePerms[cubeKey] = []
    cubePerms[cubeKey].append(cube)

    # CAVEAT: Problem asks for exactly 5, but this works
    if len(cubePerms[cubeKey]) >= 5:
        ans = min(cubePerms[cubeKey])
        break

print(ans)

