# Uses python3
import sys


def fibonacci_sum_fast(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    _sum     = 1
    # pisano period of mod 10 is 60

    for _ in range(n - 1):
        previous, current = current, (previous + current) % m
        _sum = _sum + current
        if previous == 0 and current == 1:
            p_length = _+1
            _sum_period = _sum - (current + previous)
            # print (p_length)
            return (n//p_length) * (_sum_period % 10) + fibonacci_sum_fast(n % p_length, m)
            # with m=2, F_4 is the iteration where the pattern repeats, and length is n-2, or _+2-1 = _
    return _sum % 10


if __name__ == '__main__':
    input = sys.stdin.readline()
    n = int(input)
    print(fibonacci_sum_fast(n, 10))
