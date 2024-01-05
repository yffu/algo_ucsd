#Uses python3

import sys
Debug = False


class Clock:
    def __init__(self, num_adj):
        self.i = 1
        self.pre = [0] * num_adj
        self.post = [0] * num_adj
        self.cycle = 0

    def previsit(self, v):
        self.pre[v] = self.i
        self.i += 1

    def postvisit(self, v):
        self.post[v] = self.i
        self.i += 1


def acyclic(adj):
    # Output 1 if the graph contains a cycle and 0 otherwise.
    # last vertex in the ordering cannot have any edges pointing out of it.
    # there should be a sink. Follow path as far as possible. eventually either:
    # cannot extend (found sink)
    # repeat a vertex (have a cycle)
    # has no cycles > directed acyclic graph > can be linearly ordered
    if Debug: print('adj: ', adj)
    return linear_order(adj, Clock(len(adj)))


def linear_order(adj, c):
    for v in range(len(adj)):
        if c.pre[v] == 0:
            explore(v, adj, c)
    return c.cycle


def explore(v, adj, c):
    c.previsit(v)
    if Debug:
        print('v: ', v)
        print('pre: ', c.pre)
    for w in adj[v]:
        if Debug: print('w: ', w)
        if c.pre[w] == 0: # w not visited
            explore(w, adj, c)
        elif c.pre[w] < c.pre[v] and c.post[w] == 0:
            # post[w] == 0 > in current call to explore
            # c.pre[w] < c.pre[v] > new node has been found before current node
            if Debug: print('cycle found: ')
            c.cycle = 1
    c.postvisit(v)
    if Debug: print('post: ', c.post)


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))

# 04
# Correct output:
# 1
