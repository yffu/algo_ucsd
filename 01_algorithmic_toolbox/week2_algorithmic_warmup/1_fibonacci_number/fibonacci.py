# Uses python3
def calc_fib(num):
    if num <= 1:
        return num

    return calc_fib(num - 1) + calc_fib(num - 2)


if __name__ == '__main__':
    n = int(input())
    print(calc_fib(n))
