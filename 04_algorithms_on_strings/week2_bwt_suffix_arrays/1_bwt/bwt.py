# python3
import sys


def BWT(text):
    m = list()
    len_t = len(text)
    for i in range(len_t):
        m.append(text[-i:]+text[:-i])
    m.sort()
    # print(m)
    bwt = ''
    for t in m:
        bwt += t[len_t-1]
    return bwt


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
