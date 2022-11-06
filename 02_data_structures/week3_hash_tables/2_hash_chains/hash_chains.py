# python3

class Query:

    def __init__(self, query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])    # index to check
        else:
            self.s = query[1]   # string to check


class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self, bucket_count):
        self.bucket_count = bucket_count
        # store all strings in one list
        self.elems = [list() for i in range(self.bucket_count)]

    def _hash_func(self, s):
        # polynomial hash function
        ans = 0
        for c in reversed(s):
            ans = (ans * self._multiplier + ord(c)) % self._prime
        return ans % self.bucket_count

    def write_search_result(self, was_found):
        print('yes' if was_found else 'no')

    def write_chain(self, chain):
        print(' '.join(chain))

    def read_query(self):
        # read single line of query form input
        return Query(input().split())

    def process_query(self, query):
        # process parsed results form read_query
        if query.type == "check":
            # use reverse order, because we append strings to the end
            # Note that you need to output a blank line when you handle an empty chain.
            self.write_chain(self.elems[query.ind])
        else:
            try:
                # ind = self.elems.index(query.s)     # index of the string to find
                chain = self.elems[self._hash_func(query.s)]
                ind = chain.index(query.s)
            except ValueError:
                ind = -1
            if query.type == 'find':
                self.write_search_result(ind != -1)
            elif query.type == 'add':
                if ind == -1:
                    # self.elems.append(query.s)      # just added to the end.
                    # When inserting a new string into a hash chain, you must insert it in the beginning of the chain.
                    chain.insert(0, query.s)
            elif query.type == 'del':
                if ind != -1:
                    # self.elems.pop(ind)
                    chain.pop(ind)
            else:
                None

    def process_queries(self):
        n = int(input())
        for i in range(n):
            self.process_query(self.read_query())   # second line is number of queries


if __name__ == '__main__':
    bucket_count = int(input())     # first line is number of buckets, or the cardinality of the hash table
    proc = QueryProcessor(bucket_count)
    proc.process_queries()
