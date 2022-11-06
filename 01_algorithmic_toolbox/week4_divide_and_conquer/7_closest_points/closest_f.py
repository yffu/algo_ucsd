#Uses python3
import sys
import math
debug = True


def min_dist(pts):
    n = len(pts)
    if n == 2:
        # base case with only 1 point -
        return pow(pow(x[1]-x[0], 2)+pow(y[1]-y[0], 2), 1/2)
    elif n == 3:
        return min(pow(pow(x[2]-x[1], 2)+pow(y[2]-y[1], 2), 1/2), pow(pow(x[1]-x[0], 2)+pow(y[1]-y[0], 2), 1/2), pow(pow(x[2]-x[0], 2)+pow(y[2]-y[0], 2), 1/2))

    mid = n // 2
    l_pts = pts[0:mid]
    r_pts = pts[mid:n]

    d = min(min_dist(l_pts), min_dist(r_pts))
    l_end = len(l_pts) - 1
    r_beg = 0
    mid_x = (r_pts[r_beg][0] + l_pts[l_end][0])/2

    strip = []
    while l_end >= 0:
        if mid_x - l_pts[l_end][0] <= d:
            strip.insert(0, (l_pts[l_end][0], l_pts[l_end][1]))
        else:
            break
        l_end -= 1
    while r_beg < len(r_pts):
        if r_pts[r_beg][0] - mid_x <= d:
            strip.append((r_pts[r_beg][0], r_pts[r_beg][1]))
        else:
            break
        r_beg += 1
    strip.sort(key=lambda x: x[1])

    for i in range(len(strip)):
        pt1 = strip[i]
        for j in range(i+1, len(strip)):
            if j - i > 7:
                break
            else:
                pt2 = strip[j]
                d = min(d, pow(pow(pt1[0]-pt2[0], 2)+pow(pt1[1]-pt2[1], 2), 1/2))

    return d


def minimum_distance(x, y):
    #write your code here
    # split grid into 2 sections, each with size n/2
    # recursive call to each section, and take the minimum of the distance d1 and d2, as d
    # check if points between segments whose distance is smaller than d. discard points whose distance from middle is greater than d
    pts = []
    n = len(x)
    for i in range(n):
        pts.append((x[i], y[i]))
    pts.sort(key= lambda x: (x[0], x[1]))
    return min_dist(pts)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
