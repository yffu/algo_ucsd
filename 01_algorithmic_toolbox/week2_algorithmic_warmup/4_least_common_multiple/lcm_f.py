# Uses python3
import sys


def lcm_fast(a, b):
    gcd = gcd_fast(a, b)
    return (a * b)//gcd


def gcd_fast(a, b):
    a, b = max(a, b), min(a, b)
    r = a % b
    if r == 0:
        return b
    else:
        return gcd_fast(b, r)


if __name__ == '__main__':
    input = sys.stdin.readline()
    a, b = map(int, input.split())
    print(lcm_fast(a, b))

