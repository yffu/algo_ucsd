# python3
from random import randint
debug = False


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]


class Param:
    def __init__(self, p, m):
        self.p = p
        self.m = m
        self.a = randint(1, p-1)
        self.b = randint(0, p-1)
        if debug:
            print('p: ' + str(self.p))
            print('m: ' + str(self.m))
            print('a: ' + str(self.a))
            print('b: ' + str(self.b))

    def get_index(self, x):
        return ((self.a * x + self.b) % self.p) % self.m


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]


def write_responses(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    param = Param(10000019, len(queries))
    contacts = [list() for i in range(param.m)]
    for cur_query in queries:
        i = param.get_index(cur_query.number)
        chain = contacts[i]
        if debug:
            print(contacts)
            print('operation: ' + cur_query.type + ' number: ' + str(cur_query.number))
            print('chain at ' + str(i) + ': ' + str(chain))
        found = None
        for j in range(len(chain)):
            if debug:
                print('contact in query', cur_query.number, sep=', ')
                print('contact in chain', chain[j].name, chain[j].number, sep=', ')
            if chain[j].number == cur_query.number:
                found = j
                break
        # found is index of item with matching number, or None if not no item match
        if debug: print('found: ', found, sep=', ')
        if cur_query.type == 'add':
            if found is not None:
                chain[found].name = cur_query.name
            else:
                chain.append(cur_query)
        elif cur_query.type == 'del':
            if found is not None:
                chain.pop(found)
            else:
                None
        elif cur_query.type == 'find':
            if found is not None:
                result.append(chain[found].name)
            else:
                result.append('not found')
        else:
            None
    return result


if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

