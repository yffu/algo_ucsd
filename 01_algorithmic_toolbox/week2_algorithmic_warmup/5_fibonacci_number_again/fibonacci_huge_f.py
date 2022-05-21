# Uses python3
import sys


def fibonacci_huge_fast(n, m):

    if n <= 1:
        return n
    # when
    previous = 0
    current = 1

    # iterate from F_2 to F_n , or _ from 0 to n-2 (if you shift by -2), to convert from _ to n, shift by +2
    # with F_2, prev = 1, curr = 1
    # with F_3, prev = 1, curr = 0
    # with F_4, prev = 0, curr = 1 -> this is the recurring pattern at start
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m
        if previous == 0 and current == 1:
            p_length = _+1
            # print (p_length)
            return fibonacci_huge_fast(n % p_length, m)
            # with m=2, F_4 is the iteration where the pattern repeats, and length is n-2, or _+2-1 = _
    return current


if __name__ == '__main__':
    input = sys.stdin.readline();
    n, m = map(int, input.split())
    print(fibonacci_huge_fast(n, m))
