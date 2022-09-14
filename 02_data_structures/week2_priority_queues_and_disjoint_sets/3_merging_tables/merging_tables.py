# python3
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


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst - 1, src - 1)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
