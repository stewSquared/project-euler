/**2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?

*/


def lcm(m: Int, n: Int) =
    (for (k <- (m to m*n by m).iterator if k%n == 0) yield k).next

1 to 20 reduce lcm
