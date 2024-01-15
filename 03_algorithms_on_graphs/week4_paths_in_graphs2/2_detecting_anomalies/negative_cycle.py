#Uses python3

import sys
import queue
import math
Debug = False


def negative_cycle(adj, cost):
    #write your code here
    if Debug:
        print("adj: " + str(adj))
        print("cost: " + str(cost))
    dist = [None] * len(adj)
    prev = [None] * len(adj)
    i = 0
    while i < len(adj) - 1:
        relax_in_iteration = False
        for u in range(len(adj)):
            if dist[u] is None:
                dist[u] = 0
            if Debug:
                print(f"u: {u}, dist {dist[u]}, iteration {i}")
            for j in range(len(adj[u])):
                v = adj[u][j]
                cost_uv = cost[u][j]
                # cost_uv = math.log2(cost_uv) weights are already in logarithm units.
                if Debug: print(f"adj edge v before: {v}, dist: {dist[v]}, cost: {cost[u][j]}")
                if dist[v] is None or dist[v] > dist[u] + cost_uv:
                    if Debug: print("relax")
                    dist[v] = dist[u] + cost_uv
                    prev[v] = u
                    relax_in_iteration = True
                    # after as many iterations as there is vertices of bellman-ford, the last v can still be relaxed, means that it is on a negative cycle. otherwise the distance should not be able to relax
                if Debug: print(f"adj edge v after: {v}, dist: {dist[v]}, cost: {cost[u][j]}")
        if Debug:
            print("dist: ", dist)
            print("prev: ", prev)
        if relax_in_iteration:
            i += 1
        else:
            return 0
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))
