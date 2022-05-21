# Uses python3
debug = True


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def MinAndMax(i, j, d_min, d_max):
    min = None
    max = None
    for k in range(i, j-1):
        a = d_min
    return 0, 0


def get_maximum_value(dataset):
    #write your code here
    n = len(dataset)//2 + 1
    d_min = [[0] * n for i in range(n)]
    d_max = [[0] * n for i in range(n)]

    for i in range(n):
        d_min[i][i] = dataset[i * 2]
        d_max[i][i] = dataset[i * 2]
    if debug:
        print(d_min)
        print(d_max)
    for s in range(n-1):
        for i in range(n-s):
            j = i + s
            d_min[i][j], d_max[i][j] = MinAndMax(i, j, d_min, d_max)

    return d_max[i][n-1]


if __name__ == "__main__":
    print(get_maximum_value(input()))
