"""Starting in the top left corner of a 2x2 grid, and only being able
to move to the right and down, there are exactly 6 routes to the
bottom right corner.

How many such routes are there through a 20x20 grid?

"""
def paths(x, y, cache={}):
    if x == 0 or y == 0: return 1
    if (x,y) not in cache:
        cache[(x,y)] = paths(x, y-1) + paths(x-1, y)
    return cache[(x,y)]
        
ans = paths(20,20)

print(ans)
