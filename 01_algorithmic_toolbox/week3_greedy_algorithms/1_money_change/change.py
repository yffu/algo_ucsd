# Uses python3
import sys


def get_change(m):
    # write your code here
    # output the minimum number of coins to make change.
    # coins are 1, 5, 10
    if m >= 10:
        m -= 10;
    elif m >= 5:
        m -= 5
    elif m >= 1:
        m -= 1
    else:
        return 0
    return 1 + get_change(m)


if __name__ == '__main__':
    m = int(sys.stdin.readline())
    print(get_change(m))
