"""Work out the first ten digits of the sum of the following
one-hundred 50-digit numbers.

[p013.txt]

"""

str(sum(int(line) for line in open("p013.txt")))[:10]

print(ans)
