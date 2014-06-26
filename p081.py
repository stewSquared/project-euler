"""Find the minimal path sum, in matrix.txt, a 31K text file
containing a 80 by 80 matrix, from the top left to the bottom right by
only moving right and down.

"""

grid = [eval("[{}]".format(line))[::-1] for line in open("p081.txt")][::-1]

for k in range(1, len(grid)):
    grid[0][k] += grid[0][k-1]
    grid[k][0] += grid[k-1][0]

for i in range(1,len(grid)):
    for j in range(1,len(grid)):
        grid[i][j] += min(grid[i-1][j], grid[i][j-1])

ans = grid[-1][-1]

print(ans)
