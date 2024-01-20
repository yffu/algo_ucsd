#Uses python3
import sys
import math
import queue
debug = False


def minimum_distance(x, y):
    cost = list()
    parent = list()
    graph = list()
    pqueue = queue.PriorityQueue()
    for i in range(len(x)):
        cost.append(10**19)
        parent.append(-1)
    if debug:
        print("x: " + str(x))
        print("y: " + str(y))
        print("cost: " + str(cost))
        print("parent: " + str(parent))

    u_0 = 0
    cost[u_0] = 0
    parent[u_0] = u_0
    pqueue.put((0, u_0))
    while not pqueue.empty():
        c, v = pqueue.get()
        if debug:
            print(f"pqueue item: vertex {v} cost {c}")
        if c > cost[v]:
            continue
            print(f'continue on vertex {v}: cost: {cost[v]}')
        graph.append(v)
        for z in range(0, len(x)):
            if z in graph:
                continue
            d = math.sqrt(pow(x[z]-x[v], 2) + pow(y[z]-y[v], 2))
            if debug:
                print(f"distance from {v} to {z}: {d} ")
            if cost[z] > d:
                if debug: print(f"found shorter {z} old cost {cost[z]} new cost {d} ")
                cost[z] = d
                parent[z] = v
                pqueue.put((d, z))
        if debug:
            print(f"cost: {cost}")
            print(f"parent: {parent}")
            print(f"queue: {list(pqueue.queue)}")

    # write your code here
    # use prim's algorithm
    return sum(cost)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
