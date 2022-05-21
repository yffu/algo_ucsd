# Uses python3
import sys
import itertools
debug = False

# Constraints. 1 ≤ 𝑛 ≤ 20, 1 ≤ 𝑣𝑖 ≤ 30 for all 𝑖.


def partition3(A):
    if sum(A) % 3 != 0:
        return 0
    W = sum(A)//3
    w_13 = list()
    w_23 = list()
    # w_gt = list() don't keep the greater than W lists, since we don't continue with them and they'll be excluded from w_lt.
    w_lt = [[]]
    w_comp = [A]
    # 2 ^ n combinations, sort into bags: equal to W, less than W, or greater than W
    # base is with only 1 item in set. there needs to be 3 sets equal to W, and all disjoint
    # the ones that did reach W//3, check the complement for another W//3.
    # but now you have all the ones that add to W//3, how do you tell which ones are disjoint? there's no continuity there.
    for v in A:
        for ind in range(len(w_lt)):
            newset = [x for x in w_lt[ind]]
            compset = [x for x in w_comp[ind]]
            newset.append(v)
            compset.remove(v)
            newsum = sum(newset)
            if newsum == W:
                w_13.append(newset)
                w_23.append(compset)
            elif newsum < W:
                w_lt.append(newset)
                w_comp.append(compset)
            else:
                None
            if debug:
                print("W is: {0}; v is: {1}; newsum is: {2} ".format(W, v, newsum))
                print("newset is: {0} and compset is: {1} ".format(newset, compset))
                print(w_lt)
                print(w_comp)
    if debug:
        print(w_13)
        print(w_23)
    # for each item in w_13, take corresponding item in w_23 and check the rest of w_13 to see if all elements of w_13 are in w_23

    while w_13 and w_23:
        v_13 = w_13.pop()
        v_23 = w_23.pop()
        if debug:
            print(v_13)
            print(v_23)
        for v in w_13:
            if all(item in v_23 for item in v):
                return 1
            else:
                None
    return 0

    #Attempt 2
    '''
    if sum(A) % 3 != 0:
        return 0
    cnt, w_sum, w_target = 0, 0, sum(A)//3
    for a in A:
        w_sum += a
        # there must be one that contains the first element,
        if w_sum == w_target:
            w_sum = 0
            cnt += 1
    return cnt >= 3
    '''
    #Attempt 1
    '''
    W = 0
    if sum(A) % 3 != 0:
        return 0
    else:
        W = sum(A)//3

    cnt = 0
    while cnt < 3:
        d = list()
        d.append([0] * (W+1))
        for i in range(1, len(A) + 1):
            d.append([0])
        if debug:
            print(A)
            print("W is {0}: ".format(W))
            print(d)
        for i in range(1, len(A) + 1):
            for wt in range(1, W+1):
                d[i].append(d[i-1][wt])
                if A[i-1] <= wt:
                    val = d[i-1][wt-A[i-1]] + A[i-1]
                    if d[i][wt] < val:
                        d[i][wt] = val
        if debug:
            print("after: ")
            for row in d:
                print(row)
            print("A is {0} and W is {1}".format(len(A), W))
        if d[len(A)][W] != W:
            return 0
        else:
            wt = W
            A_picked = [0] * len(A)
            for i in reversed(range(1, len(A)+1)):
                print ("i is {0} and wt is {1}".format(i, wt))
                a_0 = d[i - 1][wt]
                a_wt_0 = d[i - 1][wt-A[i - 1]]
                if wt == a_wt_0 + A[i - 1]:
                    A_picked[i - 1 ] = 1
                    wt -= A[i - 1]
                else:
                    A_picked[i - 1] = 0
        if debug:
            print(A_picked)
            print(A)
        A = [x for ind, x in enumerate(A) if A_picked[ind] == 0]
        cnt += 1
    return 1
    '''


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

