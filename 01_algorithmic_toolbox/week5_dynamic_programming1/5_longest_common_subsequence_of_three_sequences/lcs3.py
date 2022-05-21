#Uses python3

import sys
debug = False


def lcs3(a, b, c):
    #write your code here
    d = []
    for i in range(len(c)+1):
        d.append([])
        for j in range(len(b)+1):
            d[i].append([])
            for k in range(len(a)+1):
                #print("i: {0}; j: {1}; k: {2}".format(i, j, k))
                #if (i == 0 and j == 0) or (i == 0 and k == 0) or (j == 0 and k == 0):
                if i == 0 or j == 0 or k == 0:
                    d[i][j].append(0)
                else:
                    d_mat = d[i-1][j-1][k-1] + (1 if c[i-1] == b[j-1] == a[k-1] else 0)
                    d_ins1 = max(d[i-1][j][k], d[i][j-1][k], d[i][j][k-1])
                    d_ins2 = max(d[i-1][j-1][k], d[i-1][j][k-1], d[i][j-1][k-1])
                    d[i][j].append(max((d_mat, d_ins1, d_ins2)))
                    #d[i][j].append(1)
                    if debug:
                        print("i: {0}; j: {1}; k: {2}".format(i, j, k))
                        for i_slice in d:
                            print()
                            for j_slice in i_slice:
                                print(j_slice)
            '''
            elif j == 0:
                d[i].append(0)
            else:
                d_ins = d[i][j-1]
                d_del = d[i-1][j]
                d_mat = d[i-1][j-1] + (1 if a[j-1] == b[i-1] else 0)
                d[i].append(max(d_ins, d_del, d_mat))
            '''
    return d[-1][-1][-1]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
