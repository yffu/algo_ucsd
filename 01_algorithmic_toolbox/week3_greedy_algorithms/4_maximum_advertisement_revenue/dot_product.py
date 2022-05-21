#Uses python3

import sys


def max_dot_product(a, b):
    # write your code here
    res = 0
    # Greedy choice -> take a with largest absolute value, then the largest b with the same sign.
    # Greedy choice -> take cross product of all a and b, then find largest a * b, then add to res.
    # Prove that it's a sae move -> it has to be the largest a * b for the next step.
    # Reduce to a subproblem -> pop off the a and b that resulted in largest a * b, then regenerate grid of cross product.
    # Return to Greedy choice.
    # A
    #  5 3 1
    # -1 1 1
    # B
    #  4 2  1
    #  1 -1 1
    '''
    # Attempt 1
    a_factor = []
    b_factor = []
    for i in range(len(a)):
        if a[i] < 0:
            a_factor.append((-a[i], -1))
        else:
            a_factor.append((a[i], 1))
        if b[i] < 0:
            b_factor.append((-b[i], -1))
        else:
            b_factor.append((b[i], 1))
    a_factor.sort(key=lambda x: x[0], reverse=True)
    b_factor.sort(key=lambda x: x[0], reverse=True)
    print(a_factor)
    print(b_factor)
    # [(1, 1), (3, 1), (5, -1)]
    # [(2, -1), (4, 1), (1, 1)]
    '''

    # Attempt 2
    # Failed case #30/41: time limit exceeded (Time used: 10.00/5.00, memory used: 95203328/536870912.)
    # Need to optimize

    '''
    while a:
        prod = []
        for i in a:
            for j in b:
                prod.append((i*j, i, j))
        prod.sort(key=lambda x: x[0], reverse=True)
        prod_lg = prod[0]
        res += prod_lg[0]
        a.remove(prod_lg[1])
        b.remove(prod_lg[2])
    '''

    '''
     -2  4  1
    1  [[-2, 4, 1], 
    3  [-6, 12, 3], 
    -5 [10, -20, -5]]
    '''
    '''
    prod_grid = []
    for i in a:
        prod_row = []
        for j in b:
            prod_row.append(i*j)
        prod_grid.append(prod_row)

    print(max(prod_grid))
    '''

    # Attempt 3
    # Failed case #30/41: time limit exceeded (Time used: 9.99/5.00, memory used: 118996992/536870912.)
    '''
    prod = []
    for i in range(len(a)):
        for j in range(len(b)):
            prod.append((a[i]*b[j], i, j))
    prod.sort(key=lambda x: x[0])
    while prod:
        prod_max = prod.pop()
        res += prod_max[0]
        row = prod_max[1]
        col = prod_max[2]
        # print(prod)
        # delete all the record with i = row, j = col
        prod = [p for p in prod if p[1] != row]
        prod = [p for p in prod if p[2] != col]
        # print(prod)
        # print(prod_max)
    '''
    a.sort(key=lambda x: x)
    b.sort(key=lambda x: x)
    # print(a)
    # print(b)
    while a:
        res += a.pop() * b.pop()
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
    
