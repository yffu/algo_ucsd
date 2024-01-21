#Uses python3

import sys
import queue
Debug = False


def bipartite(adj):
    #write your code here
    # DONE, might need to consider graphs with parts that are not connected
    #a graph is bipartite if its vertices can be colored with two colors
    #(say, black and white) such that the endpoints of each edge have different colors.
    #Adapt the breadth-first search to solve this problem.
    # 03 should return 0, it is combination of 01 and 03
    # 04 should return 1, it is 04 with 6-7 edge removed
    if Debug: print("adj: " + str(adj))
    part = [-1] * len(adj)
    q = list()
    for v in range(len(adj)):
        if part[v] == -1:
            q.append(v)
            part[v] = 0
        while q:
            u = q.pop(0)
            if Debug: print("dequeue u: " + str(u))
            for v in adj[u]:
                if part[v] == -1:
                    if Debug: print("enqueue v: " + str(v))
                    q.append(v)
                    part[v] = 1 if part[u] == 0 else 0
                else:
                    if Debug: print("previously found v: " + str(v))
                    if part[u] == part[v]:
                        return 0
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
