"""Considering natural numbers of the form, ab, where a, b < 100, 
what is the maximum digital sum?"""

ans = max(sum(int(c) for c in str(a**b)) for a in range(100) for b in range(100))

print(ans)
