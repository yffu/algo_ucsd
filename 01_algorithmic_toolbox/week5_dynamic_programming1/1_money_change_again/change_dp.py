# Uses python3
import sys
debug = False


def get_change(m):
    #write your code here
    # denominations 1 3 4
    # [ 1 # 1 1 ]
    # return minimum number of coins
    cnt = [0] * m
    cnt[0] = 1
    if m - 1 >= 2:
        cnt[2] = 1
    if m - 1 >= 3:
        cnt[3] = 1
    #  1 ≤ money ≤ 10^3
    # go from 0 to m-1
    # if there is a value, skip it; if there is no value, then take the value at prev position 1, 3, 4 and calculate minimum
    for i in range(m):
        min_cnt = cnt[i]
        if min_cnt != 0:
            continue
        min_cnt = cnt[i-1]
        if i > 2:
            min_cnt = min(min_cnt, cnt[i-3])
        if i > 3:
            min_cnt = min(min_cnt, cnt[i-4])
        cnt[i] = min_cnt + 1
    if debug: print(cnt)
    return cnt[m-1]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
