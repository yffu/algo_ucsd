# Uses python3
import sys
debug = False


def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    #divide -> mergesort solution with start and points
    # list of start A, list of points B, list of ends C: assumed to be sorted ascending
    # compare first element of A and B for smaller element:
    # if it's A, and first one overlap cnt = 1 and set prev to index of A
    # if it's A, and not the first one increase overlap cnt += 1
    # if it's B, check from prev A to current A to see how many endpoints have passed
    all_pts = []
    for i in range(len(starts)):
        all_pts.append((starts[i], 0, i))
    for i in range(len(points)):
        all_pts.append((points[i], 1, i))
    for i in range(len(ends)):
        all_pts.append((ends[i], 2, i))

    all_pts.sort(key=lambda x: (x[0], x[1]))
    if debug: print(all_pts)
    overlap = 0
    for i in range(len(all_pts)):
        pt = all_pts[i]
        if pt[1] == 0:
            # start pt
            overlap += 1
        elif pt[1] == 1:
            # lottery pt
            cnt[pt[2]] = overlap
        elif pt[1] == 2:
            # end pt
            overlap -= 1
        else:
            None
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
