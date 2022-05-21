# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')
debug = False


def optimal_points(segs):
    pts = []

    # worst case scenario, as many points as there are segments
    # greedy choice -> place the point where it covers the max number of lines. (nope too complicated)
    # it's a safe move since if not there is another move that removes more lines
    # reduce to a subproblem -> move the lines where the point overlaps.

    # greedy choice, rightmost point on the leftmost segment, and pop the overlapping segment(s)
    segs.sort(key=lambda x: (x[0], x[1]))
    if debug: print(segs)
    curr_seg = 0
    while curr_seg < len(segs):
        last_seg = curr_seg
        overlap = segs[last_seg]
        pt = overlap.end
        while curr_seg < len(segs):
            if overlap.end >= segs[curr_seg].start:
                # Segment(start=25, end=27), Segment(start=26, end=26), Segment(start=26, end=28),
                # last_seg needs to be updated on each iteration, to the overlap of last_seg and curr_seg
                overlap=Segment(max(overlap.start, segs[curr_seg].start), min(overlap.end, segs[curr_seg].end))
                pt = overlap.end
            else:
                # reached out of range segment
                break
            curr_seg += 1
        if debug:
            print("last: " + str(segs[last_seg]))
            print("curr: " + str(segs[curr_seg-1]))
            print("pt: " + str(pt))

        pts.append(pt)
    return pts


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
