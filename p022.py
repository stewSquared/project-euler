"""Using names.txt (right click and 'Save Link/Target As...'), a 46K
text file containing over five-thousand first names, begin by sorting
it into alphabetical order. Then working out the alphabetical value
for each name, multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN,
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the
list. So, COLIN would obtain a score of 938

"""

names = sorted(eval('[' + next(open("p022.txt")) + ']'))

def value(name): return sum(ord(c) - 64 for c in name)

ans = sum(map(lambda name, position: value(name) * position,
              names, range(1,len(names)+1)))

print(ans)

