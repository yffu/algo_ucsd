# Uses python3
import sys
debug = False


def get_majority_element(a, left, right):
    # if a sequence of length n contains a majority element, then the same element is also a majority element for one of its halves
    if debug:
        print("a: " + str(a))
        print("l: " + str(left))
        print("r: " + str(right))
    # base case
    if left == right:
        # number of element between l and r is 0, no majority element
        return -1
    if left + 1 == right:
        # number of element between l and r is 1, that element is majority
        return a[left]
    #write your code here
    # odd number of values: right = 0, left = 3 -> mid = 1; right = 4, left = 7 -> mid = 5
    # even number of values: right = 4, left = 6 -> mid = 5; right = 0, left = 2 -> mid = 1 (0, 1) (1, 2)
    mid = (right + left)//2
    l_val = get_majority_element(a, left, mid)
    r_val = get_majority_element(a, mid, right)
    if debug:
        print("left: " + str(a[left: mid]) + " right: " + str(a[mid: right]))
        print("l_val: " + str(l_val) + " and r_val: " + str(r_val))
    if l_val == r_val:
        # left and right each have no majority, their union has no majority.
        # left and right both have majority with same value, their union has majority with same value
        return l_val
    if l_val != -1 and (right-left)//a[left:right].count(l_val) < 2:
        # left has majority, check if union has majority with left element
        return l_val
    if r_val != -1 and (right-left)//a[left:right].count(r_val) < 2:
        # 4//1 fails, 4//2 fails, 4//3 passes
        # right has majority, check if union has majority with right element
        return r_val
    # union does not have majority
    return -1


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
