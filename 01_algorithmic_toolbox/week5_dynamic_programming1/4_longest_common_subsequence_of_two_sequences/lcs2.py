#Uses python3

import sys
debug = False


def lcs2(a, b):
    #write your code here
    # number of elements of a
    # elements of a
    # number of elements of b
    # elements of b
    # the 2 lists don't have to be sorted.
    # 1 ≤ 𝑛, 𝑚 ≤ 100; −10^9 < 𝑎𝑖, 𝑏𝑖 < 10^9
    # naive solution is to iterate thru a and then thru b then increment counter when a match is found.

    d = []
    for i in range(len(b)+1):
        d.append([])
        for j in range(len(a)+1):
            if i == 0:
                d[i].append(0)
            elif j == 0:
                d[i].append(0)
            else:
                d_ins = d[i][j-1]
                d_del = d[i-1][j]
                d_mat = d[i-1][j-1] + (1 if a[j-1] == b[i-1] else 0)
                d[i].append(max(d_ins, d_del, d_mat))
                if debug:
                    print("i: {0} and j: {1}".format(i, j))
                    print("     "+str(a))
                    for row in range(len(d)):
                        print(str(b[row-1] if row > 0 else " ") + " " + str(d[row]))
    return d[-1][-1]

    '''
    cnt = 0
    #a.sort(reverse=True)
    #b.sort(reverse=True)
    while a and b:
        a_i = a.pop()
        b_j = b.pop()
        print("comparing a: {0} and b: {1}".format(a_i, b_j))
        if a_i == b_j:
            cnt += 1
        elif a_i > b_j:
            a.append(a_i)
        else:
            b.append(b_j)
    return cnt
    '''


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
