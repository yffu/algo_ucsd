# Uses python3
import sys


def optimal_summands(n):
    summands = []
    i = 1
    #greedy choice - reduce n by the smallest integer i that has not been used.
    #special consideration: if after reducing n by i, and the remainder r is less than i+1 (the next loop)
    #then just return n as the next summand.
    while n != 0:
        if n-i < i+1:
            summands.append(n)
            n -= n
            #break loop
        else:
            summands.append(i)
            n -= i
            i += 1

    #safe move? - maximizes the remaining n after reduction
    #subproblem - start over with n-i, add i to list of used integer
    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
