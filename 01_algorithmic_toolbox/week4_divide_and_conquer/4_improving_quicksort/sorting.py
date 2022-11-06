# Uses python3
import sys
import random
debug = False


def partition3(a, l, r):
    # 6 4 6 2 9 3 9 4 7 6 1
    # 6 4 6 2 9 3 9 4 7 6 1
    # i = 2, j1 = 1, j2 = 2
    # 6 4 2 6 9 3 9 4 7 6 1
    if debug:
        print ("l: " + str(l) + " r: " + str(r) + " a: " + str(a))
    x = a[l]
    # j1 is index of last smallest element
    # j2 is index of last equal element
    j1 = l
    j2 = l
    for i in range(l+1, r+1):
        if debug:
            print(a)
            print("i: " + str(i) + " j1: " + str(j1) + " j2: " + str(j2))
        if a[i] < x:
            if debug: print("smaller element found")
            # smaller element found,
            j1 += 1
            j2 += 1
            # smaller element to end of small segment
            a[i], a[j1] = a[j1], a[i]
            # equal element to end of equal segment
            if j1 != j2:
                # if there is a segment of equal elements
                a[i], a[j2] = a[j2], a[i]
        elif a[i] == x:
            if debug: print("equal element found")
            # equal element found, increase index of rightmost equal element. swap so larger element takes new element place
            j2 += 1 # j2 = 2
            a[i], a[j2] = a[j2], a[i]
        else:
            # larger element found
            if debug: print("larger element found")
        if debug: print(a)
    a[l], a[j1] = a[j1], a[l]
    return j1, j2


def partition2(a, l, r):
    # 6 4 8 2 9 3 9 4 7 6 1
    x = a[l]
    # l = 0,x = 6
    j = l
    # j = 0, it is the partition index
    for i in range(l + 1, r + 1):
        # scan from 1 to the index of the last element
        if a[i] <= x:
            j += 1
            # smaller element found, move partition up j = 1
            # smaller element found at i = 3 a[i] = 2, j moved to 2, a[i]:2 and a[j]:8 will be swapped.
            a[i], a[j] = a[j], a[i]
    # exit the for loop, swap j and l, the larges index of the smaller numbers with the pivot number.
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    j1, j2 = partition3(a, l, r)
    randomized_quick_sort(a, l, j1 - 1);
    randomized_quick_sort(a, j2 + 1, r);
    #m = partition2(a, l, r)
    #randomized_quick_sort(a, l, m - 1);
    #randomized_quick_sort(a, m + 1, r);


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
