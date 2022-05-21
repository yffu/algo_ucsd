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


def fibonacci_partial_sum_fast(n0, n1, m):
    # pre-condition: n0 <= n1
    if n0 == 0:
        sum0 = fibonacci_sum_fast(n0, m)
    else:
        sum0 = fibonacci_sum_fast(n0-1, m)
    sum1 = fibonacci_sum_fast(n1, m)
    # print("sum1 : " + str(sum1))
    # print("sum0 : " + str(sum0))
    return (sum1-sum0) % m


if __name__ == '__main__':
    input = sys.stdin.readline();
    fr, to = map(int, input.split())
    print(fibonacci_partial_sum_fast(fr, to, 10))
