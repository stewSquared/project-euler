from functools import reduce
from operator import mul
def product(listInts): return reduce(mul, listInts)

grid = [[int(n) for n in line.rstrip('\n').split(' ')] for line in open("p011.txt")]
width, height = len(grid[0]), len(grid)

sequences = []

for seq in ([grid[row+i][col] for i in range(4)]
            for row in range(height - 4)
            for col in range(width)):
    sequences.append(seq)

for seq in ([grid[row][col+i] for i in range(4)]
            for row in range(height)
            for col in range(width - 4)):
    sequences.append(seq)

for seq in ([grid[row+i][col+i] for i in range(4)]
            for row in range(height - 4)
            for col in range(width - 4)):
    sequences.append(seq)

for seq in ([(grid[::-1])[row+i][col+i] for i in range(4)]
            for row in range(height - 4)
            for col in range(width - 4)):
    sequences.append(seq)

ans = max(product(seq) for seq in sequences)

print(ans)
