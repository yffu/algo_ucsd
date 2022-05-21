# Uses python3
import sys


def get_fibonacci_last_digit_naive(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        # tuple packing and unpacking
        # previous is set to current and current is set to previous + current
        previous, current = current, previous + current

    return current % 10


if __name__ == '__main__':
    num = int(input())
    print(get_fibonacci_last_digit_naive(num))
