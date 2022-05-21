# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    # print(capacity)
    # print(weights)
    # print(values)
    # print(len(weights))
    # iterate all weights, values, and store val/wgt and sort in desc order
    value = 0
    items = list()
    for _ in range(len(weights)):
        # val.wgt, value, weight
        items.append((values[_]/weights[_], values[_], weights[_]))

    items.sort(key=lambda x: x[0])
    items.reverse()

    for it in items:
        # print(it[0])
        # weight is less than capacity
        if it[2] <= capacity:
            value += it[1]
            capacity -= it[2]
        # weight is greater than capacity, take a fraction
        else:
            f = capacity / it[2]
            value += f * it[1]
            capacity = f * it[2]
            # return, even if there are still items.
            return value
    # return, even if there is still capacity but out of items.
    return value


if __name__ == "__main__":
    # when using read(), hit Ctrl + D to EOF
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
