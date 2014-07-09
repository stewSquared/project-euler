def count_change_ways(amount, coins):
    return (0 if amount < 0 or not coins else
            1 if amount == 0 else
            (count_change_ways(amount, coins[1:])
             + count_change_ways(amount - coins[0], coins)))

ans = count_change_ways(200, [200, 100, 50, 20, 10, 5, 2, 1])

print(ans)
