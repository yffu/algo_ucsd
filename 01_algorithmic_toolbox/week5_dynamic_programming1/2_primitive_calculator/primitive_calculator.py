# Uses python3
import sys
debug = False


def optimal_sequence(n):
    # operations are:
    # x = x * 2
    # x = x * 3
    # x = x + 1
    # given an integer n, find the min number of operations needed to obtain the number starting from 1.
    # on the second line, output a sequence of intermediate numbers in ascending order.
    sequence = []
    # 1 ≤ 𝑛 ≤ 10^6
    cnt = [0] * n
    prev = [0] * n
    '''
    while n >= 1:
        sequence.append(n)
        if n % 3 == 0:
            n = n // 3
        elif n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
    '''

    for i in range(1,n):
        # how to trace back the sequence?
        # take the minimum # of steps to get to the position and
        num = i + 1
        i_prev = i - 1
        cnt_min = cnt[i_prev]
        if num % 2 == 0:
            if debug: print("success %2: " + str(num))
            if cnt[num//2 - 1] <= cnt_min:
                i_prev = num//2 - 1
                cnt_min = cnt[num//2-1]
        if num % 3 == 0:
            if debug: print("success %3: " + str(num))
            if cnt[num//3 -1] <= cnt_min:
                i_prev = num//3 - 1
                cnt_min = cnt[num//3-1]
        cnt[i] = cnt_min + 1
        prev[i] = i_prev
        if debug:
            print("number: " + str(num) + " index: " + str(i))
            print("cnt_min: " + str(cnt_min) + " i_prev: " + str(i_prev))
            print(cnt)
            print(prev)

    i_prev = n - 1
    while i_prev > 0:
        sequence.append(i_prev + 1)
        i_prev = prev[i_prev]
    sequence.append(1)
    return reversed(sequence)


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
