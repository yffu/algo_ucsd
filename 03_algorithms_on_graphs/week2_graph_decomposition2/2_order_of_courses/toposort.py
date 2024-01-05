#Uses python3

import sys
Debug = False
x = 0


def explore(adj, used, order, v):
    used[v] = 1
    global x
    x += 1
    if Debug: print("previsit: " + str(x))
    for w in adj[v]:
        if not used[w]:
            if Debug: print("explore w: " + str(w))
            explore(adj, used, order, w)
    x += 1
    if Debug: print("postvisit: " + str(x))
    order.append(v)


def dfs(adj, used, order):
    #write your code here
    for v in range(len(adj)):
        if Debug: print("explore v: " + str(v))
        if not used[v]:
            explore(adj, used, order, v)
    return order.reverse()


def toposort(adj):
    if Debug: print("adj: " + str(adj))
    # Compute a topological ordering of a given directed acyclic graph (DAG) with 𝑛 vertices and 𝑚 edges.
    # sort vertices by reverse post-order, largest to smallest
    used = [0] * len(adj)
    order = []
    # write your code here
    dfs(adj, used, order)
    if Debug: print("order: " + str(order))
    return order


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

