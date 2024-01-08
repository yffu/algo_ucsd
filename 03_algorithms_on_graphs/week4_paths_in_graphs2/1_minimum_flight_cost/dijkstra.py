#Uses python3

import sys
import queue
Debug = False

def distance(adj, cost, s, t):
    #write your code here
    if Debug:
        print("s: " + str(s) + " t: " + str(t))
        print("adj: " + str(adj))
        print("cost: " + str(cost))
    dist = [-1] * len(adj)
    prev = [-1] * len(adj)
    dist[s] = 0
    pqueue = queue.PriorityQueue()
    pqueue.put((0, s))
    while not pqueue.empty():
        d, u = pqueue.get()
        if Debug:
            print("pqueue item: distance {0}, vertex {1}".format(d, u))
            print("dist of vertex {0}: {1}".format(u, dist[u]))
        if d > dist[u]:   # deals with duplicate inserts that do not have minimized distance, as there's built-in method to update priority value in queue implementation
            continue
        i = 0
        for v in adj[u]:
            cost_uv = cost[u][i]
            i += 1
            if Debug: print("adj edge v before: {0}, dist: {1}, cost: {2}".format(v, dist[v], cost_uv))
            if dist[v] == -1 or dist[v] > dist[u] + cost_uv:
                dist[v] = dist[u] + cost_uv
                prev[v] = u
                pqueue.put((dist[v], v))
                if Debug: print("pqueue updated: " + str(pqueue))
            if Debug: print("adj edge v after: {0}, dist: {1}, cost: {2}".format(v, dist[v], cost_uv))
    return dist[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
