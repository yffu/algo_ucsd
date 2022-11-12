# python3
from random import randint
debug = False

class Param:
    def __init__(self, p, m):
        self.p = p
        self.m = m
        self.x = randint(1, p-1)

    def get_hash(self, s):
        ans = 0
        for c in s:
            ans = (ans * self.x + ord(c)) % self.p
        return ans % self.m


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def get_occurrences(pattern, text):
    # text > 12345; pattern > 34; len(text) > 5; len(pattern) > 2; range(4) > [0, 1, 2, 3]
    # if P =/= S probability h(P) == h(S) is at most |P|/p for a prime number p used in the polynomial hash
    # 1 <= |P| <= |T| <= 5*10^5, so p = 10000019 > 10^7  >> 5*10^5
    # probability of hash values matching substr and pattern, but the strings being not equal is:
    # [(|T|-|P|+1) |P|] / p, which can be made small by selecting p >> |T||P|
    # (|T|-|P|+1) |P| ~= (2.5 * 10^5) ^ 2 = 6.25 * 10^10
    # Total running time is O((q + [(|T|-|P|+1)|P|]/p) |P|) = O(q|P|) for p >> |T||P|
    # Use recurrence equation to precompute all hashes of substrings of |T| of length equal to |P|
    # p = 10000019 (10^7), 1000000007 (10^9), 10000000019 (10^10), 1000000000039 (10^12)
    param = Param(1000000000039, 263)
    position = []
    pHash = param.get_hash(pattern)
    h = [None for i in range(len(text) - len(pattern) + 1)]
    s = text[len(text) - len(pattern): len(text) - 1]
    h[len(text) - len(pattern)] = param.get_hash(s)
    y = 1
    for i in range(len(pattern)):
        y = (y * param.x) % param.p
    if debug:
        print('h: ', h, sep=', ')
    for i in reversed(range(len(text) - len(pattern))):
        if debug: print('i: ', i, sep=', ')
        h[i] = (param.x * h[i + 1] + ord(text[i]) - y * ord(text[i + len(pattern)])) % param.p
    if debug:
        print('h: ', h, sep=', ')
        print('y: ', y, sep=', ')
        print('s: ', s, sep=', ')
    for i in range(len(text) - len(pattern) +1):
        if pHash == h[i]:
            continue
        if text[i: i + len(pattern)] == pattern:
            position.append(i)
    '''
    # Implementation without optimization
    position = []
    pHash = param.get_hash(pattern)
    for i in range(len(text) - len(pattern) + 1):
        substr = text[i: i + len(pattern)]
        # get_index and compare, if equal then compare directly
        if param.get_hash(substr) == pHash:
            # AreEqual computed in O(|P|) time but only if hash of substr and pattern equal
            if substr == pattern:
                position.append(i)
    '''
    return position


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))

