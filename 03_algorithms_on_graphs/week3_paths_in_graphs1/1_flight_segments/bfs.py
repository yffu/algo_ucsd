#Uses python3

import sys
import queue
Debug = False

def distance(adj, s, t):
    if Debug:
        print("initial v: " + str(s))
        print("final v: " + str(t))
        print("adj: " + str(adj))
    #write your code here
    dist = [-1] * len(adj)
    dist[s] = 0
    q = [s]
    while q:
        u = q.pop(0)
        if Debug: print("dequeue u: " + str(u))
        for v in adj[u]:
            if dist[v] == -1:
                if Debug: print("enqueue v: " + str(v))
                q.append(v)
                dist[v] = dist[u] + 1
            else:
                if Debug: print("previously found v: " + str(v))
            if v == t:
                if Debug: print("found t: " + str(t))
                return dist[v]
    return dist[t]


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
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
