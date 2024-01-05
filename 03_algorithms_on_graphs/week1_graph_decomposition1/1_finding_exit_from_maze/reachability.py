#Uses python3

import sys
debug = False


def reach(adj, x, y):
    #write your code here
    if debug:
        print("x: " + str(x))   # vertex to check if connected
        print("y: " + str(y))   # vertex to check if connected
    visited = [0] * len(adj)
    explore(x, adj, visited)    # x and y already zero indexed
    return visited[y]


def explore(v, adj, visited):
    visited[v] = 1
    if debug:
        print("explore: " + str(v))
        print("visited: " + str(visited))
    for w in adj[v]:
        if visited[w] == 0:
            explore(w, adj, visited)    # depth first search, only backtrack if there are no more unvisited neighbors


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    # edge list
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    if debug:
        print("n: " + str(n))
        print("m: " + str(m))
        print("edges: " + str(edges))
    x, y = data[2 * m:]
    # adjacency list
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1     # change to zero indexed
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    if debug:
        print("adj: " + str(adj))
    print(reach(adj, x, y))
