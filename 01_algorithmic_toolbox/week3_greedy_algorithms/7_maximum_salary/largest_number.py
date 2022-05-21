#Uses python3

import sys
from math import ceil
debug = False

def largest_number(a):
    #write your code here
    # Attempt 1
    '''
    res = ""
    a.sort(reverse=True)
    #elements of a are str
    #pre-condition sorted by alpha largest first digit comes first, and 23 before 2, 231 before 23
    if debug: print(a)

    for i in range(len(a)):
        x = a[i]
        #greedy choice -> set of all numbers with largest first digit, already sorted so take the next one
        #safe move -> compare the different orders
        #subproblem -> proceed to next number in a, with concatenated res
        if res != "":
            if debug:
                print("res: " + res + " x: " + x)
                print("normal: " + res + x + " reverse: " + x + res)
            # '10', '10', '1', '1', another while condition until first digit does not match?
            if int(res + x) >= int(x + res):
                res = res + x
            else:
                res = x + res

        else:
            # initial case
            res = x
    '''
    # Attempt 2
    '''
    this is on the right track, but still needs work.
    # sort by first digit, then
    a.sort(key=lambda x: (x[0], -len(x), x[1:]), reverse=True)
    # largest at end ['1', '1', '10', '10']
    res = res.join(a)
    if debug: print(a)
    '''
    # Attempt 3
    # 2 numbers ->
    # compare the 1st digit, if not equal, rank by first digit and break.
    # if equal, compare the second digit and onward until there is difference
    # if 1 number is out of digits, compare the digits of the other number against 1st digit of first number
    # works after slight modifications described in https://www.geeksforgeeks.org/arrange-given-numbers-form-biggest-number-set-2/
    res = ""
    max_len = len(max(a, key=lambda x: len(x)))
    if debug: print("max len: " + str(max_len))
    a_rank = []
    for n in a:
        #1
        #rank = (n * max_len)[:max_len]
        #2
        #mult = ceil(max_len/len(n))
        #3
        mult = (max_len//len(n)) + 1
        rank = (n * mult)[:max_len + 1]
        a_rank.append((n, rank))
    a_rank.sort(key=lambda x: x[1], reverse=True)
    if debug: print("a rank: " + str(a_rank))
    res = res.join([x[0] for x in a_rank])
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
