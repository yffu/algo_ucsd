#Uses python3
import sys
import math
debug = False


def minimum_distance(x, y):
    #write your code here
    # split grid into 2 sections, each with size n/2
    # recursive call to each section, and take the minimum of the distance d1 and d2, as d
    # check if points between segments whose distance is smaller than d. discard points whose distance from middle is greater than d
    pts = []
    n = len(x)
    if n == 2:
        # base case with only 1 point -
        return pow(pow(x[1]-x[0], 2)+pow(y[1]-y[0], 2), 1/2)
    elif n == 3:
        return min(pow(pow(x[2]-x[1], 2)+pow(y[2]-y[1], 2), 1/2), pow(pow(x[1]-x[0], 2)+pow(y[1]-y[0], 2), 1/2), pow(pow(x[2]-x[0], 2)+pow(y[2]-y[0], 2), 1/2))
    if debug:
        print("x: " + str(x))
        print("y: " + str(y))
    for i in range(n):
        pts.append((x[i], y[i]))
    pts.sort(key= lambda x: (x[0], x[1]))
    mid = len(pts) // 2
    l_x, l_y = zip(*pts[0:mid])
    r_x, r_y = zip(*pts[mid:n])
    # unpack and convert
    l_x = list(l_x)
    l_y = list(l_y)
    r_x = list(r_x)
    r_y = list(r_y)
    if debug:
        print(pts)
        print(l_x)
        print(l_y)
        print(r_x)
        print(r_y)

    d = min(minimum_distance(l_x, l_y), minimum_distance(r_x, r_y))
    l_end = len(l_x) - 1
    r_beg = 0
    mid_x = (r_x[r_beg] + l_x[l_end])/2
    if debug: print("mid_x: " + str(mid_x) + " distance: " + str(d))
    strip = []
    while l_end >= 0:
        if mid_x - l_x[l_end] <= d:
            strip.insert(0, (l_x[l_end], l_y[l_end]))
        else:
            break
        l_end -= 1
    while r_beg < len(r_x):
        if r_x[r_beg] - mid_x <= d:
            strip.append((r_x[r_beg], r_y[r_beg]))
        else:
            break
        r_beg += 1
    strip.sort(key=lambda x: x[1])
    if debug:
        print("points in the strip ")
        print(strip)
    for i in range(len(strip)):
        pt1 = strip[i]
        for j in range(i+1, len(strip)):
            if j - i > 7:
                break
            else:
                pt2 = strip[j]
                d = min(d, pow(pow(pt1[0]-pt2[0], 2)+pow(pt1[1]-pt2[1], 2), 1/2))
                if debug:
                    print("pt1: " + str(pt1) + " pt2: " + str(pt2))
                    print("i: " + str(i) + " j: " + str(j) + "   d: " + str(d))
    return d


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
