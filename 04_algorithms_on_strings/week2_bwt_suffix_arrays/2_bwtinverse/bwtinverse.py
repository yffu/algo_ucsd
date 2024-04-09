# python3
import sys
debug = False

def InverseBWT_naive(bwt):
    # write your code here
    m = [""]*len(bwt)
    for i in range(len(bwt)):
        for j in range(len(m)):
            m[j] = bwt[j]+m[j]
        #print(m)
        m.sort()
    #print("bwt: {}".format(bwt))
    for s in m:
        if s[-1:] == "$":
            return s


def InverseBWT(bwt):
    bwt_sort = sorted(bwt)
    # LF(r): Let row r be the i-h occurrence of 'a' in last column
    # Then, LF(r) = r'; r': i-th row starting with 'a'
    # C(a): # of characters smaller than 'a'
    cnt_c = dict()
    cnt_i = dict()
    lf = [None] * len(bwt)
    prev = None
    for i in range(len(bwt_sort)):
        if bwt_sort[i] != prev:
            cnt_c[bwt_sort[i]] = i
        prev = bwt_sort[i]

    i = 0
    for c in bwt:
        if c in cnt_i:
            cnt_i[c] += 1
        else:
            cnt_i[c] = 1
        lf[i] = cnt_c[c] + cnt_i[c] - 1
        i += 1

    if debug:
        print("cnt_c: {}".format(cnt_c))
        print("cnt_i: {}".format(cnt_i))
        print("bwt: {}".format(bwt))
        print("lf: {}".format(lf))

    s = ""
    r = 0
    c = bwt[r]
    c_list = list()
    while c != "$":
        c_list.append(c)
        r = lf[r]
        c = bwt[r]
    c_list.reverse()
    c_list.append("$")
    return "".join(c_list)


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
