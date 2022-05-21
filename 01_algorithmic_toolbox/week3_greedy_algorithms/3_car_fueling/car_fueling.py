# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    # print(distance)
    # print(tank)

    stops.insert(0, 0)
    stops.append(distance)
    # print(stops)
    # 000 200 375 550 750 950
    num_refill = 0
    curr_refill = 0
    # position in the array x where we're currently standing
    while curr_refill < len(stops)-1:
        last_refill = curr_refill
        # either get to the end, B or the farthest reachable gas station
        while curr_refill < len(stops)-1:
            if stops[curr_refill+1]-stops[last_refill] <= tank:
                curr_refill += 1
                # print(curr_refill)
            else:
                break
        # we have checked for next furthest station
        if curr_refill == last_refill:
            return -1
        # there is a station that is further
        if curr_refill < len(stops)-1:
            num_refill += 1
    return num_refill


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
