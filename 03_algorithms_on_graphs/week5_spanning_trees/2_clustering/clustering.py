#Uses python3
import sys
import math
import queue
debug = False


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * n_tables     # initiate rank as 1 for all
        self.parents = list(range(n_tables))    # initiate parent as self for all

    def merge(self, src, dst):
        if debug:
            print('merge: src ' + str(src) + ' and dst ' + str(dst))
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)
        # merge two components
        # use union by rank heuristic
        if src_parent == dst_parent:
            return False
        n_size = self.row_counts[src_parent] + self.row_counts[dst_parent]
        if self.ranks[src_parent] > self.ranks[dst_parent]:
            self.parents[dst_parent] = src_parent
            self.row_counts[src_parent] = n_size
            self.max_row_count = max(self.max_row_count, n_size)
        else:
            self.parents[src_parent] = dst_parent
            if self.ranks[src_parent] == self.ranks[dst_parent]:
                self.ranks[dst_parent] += 1
            self.row_counts[dst_parent] = n_size
            self.max_row_count = max(self.max_row_count, n_size)
        if debug:
            print('parents: ' + str(self.parents))
            print('ranks: ' + str(self.ranks))
            print('row counts: ' + str(self.row_counts))
        # update max_row_count with the new maximum table size
        return True

    def get_parent(self, table):
        # find parent and compress path
        if self.parents[table] != table:
            self.parents[table] = self.get_parent(self.parents[table])
        return self.parents[table]


def clustering(x, y, k):
    # write your code here
    # n points on a plane
    # k non-empty subsets
    # n-k edges that don't form a cycle.
    # kruskal's is capable of getting separate subsets and not all just on the same graph.
    # d is just the value returned from the priority queue on finding the n-k th
    # make set for each vertex
    n = len(x)
    db = Database([1]*n)
    # loop set of all points and calculate distance with every combination of points, and place it in priority queue
    pqueue = queue.PriorityQueue()
    # cnt = 0
    # n-k edges that don't form a cycle
    cnt_edge = n-k
    dist_cluster = None
    if debug:
        print(f"n: {n}")
        print(f"count of edge: {cnt_edge}")
    vert = list() # the vertices that form part of graph
    for i1 in range(n):
        for i2 in range(i1+1, n):
            d = math.sqrt(pow(x[i1]-x[i2], 2) + pow(y[i1]-y[i2], 2))
            if debug:
                print(f"i1: {i1}, i2: {i2}")
                print(f"distance: {d}")
            pqueue.put((d, i1, i2))
            # cnt += 1
    # print(f"count: {cnt}") # 12C2 = 12*11/2 = 66
    if debug: print(f"queue: {list(pqueue.queue)}")
    while not pqueue.empty() and cnt_edge >= 0:
        d, u, v = pqueue.get()
        dist_cluster = d
        if debug: print(f"d: {d}, u: {u}, v:{v}")
        if db.get_parent(u) != db.get_parent(v):
            vert.append((u, v))
            db.merge(u, v)
            cnt_edge -= 1
    if debug:
        print(f"queue: {list(pqueue.queue)}")
        print(f"edges in graph: {vert}")
        print(f"distance between cluster: {dist_cluster}")
    return dist_cluster


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
