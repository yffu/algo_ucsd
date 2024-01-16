#Uses python3

import sys
import queue
Debug = False


def shortest_paths(adj, cost, s, distance, reachable, shortest):
    # if reachable[x] == 0:     print('*')          initially 0
    # if shortest[x] == 0:      print('-')          initially 1
    # else                      print(distance[x])  initially +inf
    if Debug:
        print("adj: " + str(adj))
        print("cost: " + str(cost))
        print("s: ", s)
    prev = [None] * len(adj)
    distance[s] = 0
    reachable[s] = 1
    q = [s]
    v_neg = None
    i = 0
    while i < len(adj):
        found = [0] * len(adj)
        relax_in_iteration = False
        q.append(s)
        while q:
            u = q.pop(0)
            if Debug: print(f"u: {u}, dist {distance[u]}, iteration {i}")
            for j in range(len(adj[u])):
                v = adj[u][j]
                cost_uv = cost[u][j]
                reachable[v] = 1
                if found[v] == 0:
                    q.append(v)
                    found[v] = 1
                # cost_uv = math.log2(cost_uv) weights are already in logarithm units.
                if Debug: print(f"adj edge v before: {v}, dist: {distance[v]}, cost: {cost[u][j]}")
                if distance[v] == 10**19 or distance[v] > distance[u] + cost_uv:
                    if Debug: print("relax")
                    distance[v] = distance[u] + cost_uv
                    prev[v] = u
                    relax_in_iteration = True
                    if i == len(adj) - 1:
                        v_neg = v
                        # after as many iterations as there is vertices of bellman-ford, the last v can still be relaxed, means that it is on a negative cycle. otherwise the distance should not be able to relax
                if Debug: print(f"adj edge v after: {v}, dist: {distance[v]}, cost: {cost[u][j]}")
        if Debug:
            print("dist: ", distance)
            print("prev: ", prev)
        if relax_in_iteration:
            i += 1
        else:
            break


    # write your code here
    # Failed case #4/36: Wrong answer
    if v_neg is None:
        pass
    else:
        if Debug: print(f"v on negative cycle: {v_neg}")
        j = 0
        x = v_neg
        while j < len(adj):
            x = prev[x]
            j += 1
            if Debug: print(f"x: {x}, j: {j}")
        y = x
        shortest[y] = 0
        q = [y]
        while prev[y] != x:
            y = prev[y]
            shortest[y] = 0
            q.append(y)
            # not just negative cycle, but anything reachable from negative cycle
            if Debug: print(f"x: {x}, y: {y}")

        if Debug: print(f"q: {q}")
        while q:
            u = q.pop(0)
            for v in adj[u]:
                if shortest[v] != 0:
                    shortest[v] = 0
                    q.append(v)


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortest_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])

