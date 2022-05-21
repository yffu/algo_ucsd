# Uses python3
import sys
debug = False


def get_number_of_inversions(a, b, left, right):
    # b should hold the sorted array.
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    #write your code here
    # merge the results from left and right, and return the number of inversions
    # for any element of right that gets merged before all elements of left are merged, this counts as inversion.
    i_l = left
    i_r = ave
    i_b = left
    if debug: print("left: " + str(left) + " ave: " + str(ave) + " right: " + str(right))
    while i_l < ave and i_r < right:
        v_l = a[i_l]
        v_r = a[i_r]
        if debug:
            print("before: ")
            print("i_b: " + str(i_b) + " i_l: " + str(i_l) + " i_r: " + str(i_r) + " v_l: " + str(v_l) + " v_r: " + str(v_r))
        if v_r < v_l:
            i_r += 1
            b[i_b] = v_r
            number_of_inversions += (ave - i_l)
            if debug: print("# of inv: " + str(number_of_inversions))
        else:
            i_l += 1
            b[i_b] = v_l
        i_b += 1
        if debug:
            print("after: ")
            print("i_b: " + str(i_b) + " i_l: " + str(i_l) + " i_r: " + str(i_r) + " v_l: " + str(v_l) + " v_r: " + str(v_r))
            print("a: " + str(a))
            print("b: " + str(b))
    while i_l < ave:
        v_l = a[i_l]
        b[i_b] = v_l
        i_l += 1
        i_b += 1
        # number_of_inversions += 1
        if debug: print("# of inv: " + str(number_of_inversions))
        if debug:
            print("rest of left: ")
            print("i_b: " + str(i_b) + " i_l: " + str(i_l) + " i_r: " + str(i_r) + " v_l: " + str(v_l) + " v_r: " + str(v_r))
            print("a: " + str(a))
            print("b: " + str(b))
    while i_r < right:
        v_r = a[i_r]
        b[i_b] = v_r
        i_r += 1
        i_b += 1
        if debug:
            print("rest of right: ")
            print("i_b: " + str(i_b) + " i_l: " + str(i_l) + " i_r: " + str(i_r) + " v_l: " + str(v_l) + " v_r: " + str(v_r))
            print("a: " + str(a))
            print("b: " + str(b))
    for i in range(left, right):
        a[i] = b[i]
    return number_of_inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
