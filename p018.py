"""By starting at the top of the triangle below and moving to adjacent
numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

[p018.txt]

NOTE: As there are only 16384 routes, it is possible to solve this
problem by trying every route. However, Problem 67, is the same
challenge with a triangle containing one-hundred rows; it cannot be
solved by brute force, and requires a clever method! ;o)

"""
from functools import reduce
rows = [[int(numeral) for numeral in line.split()]
        for line in open("p018.txt")][::-1]

def reduceRows(longer, shorter):
    return [(shorter[i] + max (longer[i:i+2]))
            for i in range(len(shorter))]

ans = reduce(reduceRows, rows)[0]

print(ans)
