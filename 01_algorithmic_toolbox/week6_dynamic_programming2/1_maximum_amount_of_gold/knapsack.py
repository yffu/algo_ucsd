# Uses python3
import sys
debug = False


def optimal_weight(W, w):
    # write your code here
    # single copy of each item.
    result = 0
    d = list()
    d.append([0] * (W + 1))
    for i in range(1, len(w) + 1):
        d.append([0])
    if debug:
        print("before: ")
        print(d)
    for i in range(1, len(w) + 1):
        for wt in range(1, W+1):
            d[i].append(d[i-1][wt])
            if w[i-1] <= wt:
                val = d[i-1][wt - w[i-1]] + w[i-1]
                if d[i][wt] < val:
                    d[i][wt] = val
    if debug:
        print("after: ")
        print(d)
    return d[len(w)][W]


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
