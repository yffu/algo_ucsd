# Uses python3
def calc_fib(n):
    fib_0 = 0
    fib_1 = 1
    if n == 0:
        return fib_0
    for _ in range(n-1):
        # if n = 1, return 1
        # if n = 0, return 0
        # tuple packing expression
        fib_0, fib_1 = fib_1, fib_0 + fib_1
    return fib_1


if __name__ == '__main__':
    num = int(input())
    print(calc_fib(num))
