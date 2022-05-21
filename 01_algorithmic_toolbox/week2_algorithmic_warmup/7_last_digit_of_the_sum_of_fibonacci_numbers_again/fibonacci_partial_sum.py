# Uses python3
import sys


def fibonacci_partial_sum_naive(fr, to):
    _sum = 0

    current = 0
    _next  = 1

    for i in range(to + 1):
        if i >= fr:
            _sum += current

        current, _next = _next, current + _next

    return _sum % 10


if __name__ == '__main__':
    input = sys.stdin.readline();
    fr, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(fr, to))
