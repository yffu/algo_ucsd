#Uses python3

import sys
Debug = False
x = 0

sys.setrecursionlimit(200000)


def explore(adj, used, order, v):
    used[v] = 1
    global x
    x += 1
    if Debug:
        print("previsit: " + str(x))
        print("explore v: " + str(v))
    for w in adj[v]:
        if not used[w]:
            explore(adj, used, order, w)
    x += 1
    if Debug:
        print("postvisit: " + str(x))
        #print("postorder v: " + str(v))
    order.append(v)


def explore_scc(adj, visited, v):
    visited[v] = 1
    if Debug: print("visited: " + str(visited))
    for w in adj[v]:
        if not visited[w]:
            explore_scc(adj, visited, w)


def dfs(adj, used):
    #write your code here
    order = []
    for v in range(len(adj)):
        if Debug: print("explore initial vertex: " + str(v))
        if not used[v]:
            explore(adj, used, order, v)
    order.reverse()
    return order


def number_of_strongly_connected_components(adj, adj_r):
    order = dfs(adj_r, [0] * len(adj))
    if Debug: print("vertices in reverse postorder: " + str(order))
    visited = [0] * len(order)
    cc = 0
    for v in order:
        #print("v: " + str(v))
        if not visited[v]:
            cc += 1
            explore_scc(adj, visited, v)
    #Largest remaining post number comes from sink component.
    #write your code here
    #Compute the number of strongly connected components of a given directed graph with 𝑛 vertices and 𝑚 edges.
    return cc


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    adj_r = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj_r[b - 1].append(a - 1)  # reverse graph
    if Debug:
        print("adj: " + str(adj))
        print("adj_r: " + str(adj_r))
    print(number_of_strongly_connected_components(adj, adj_r))
