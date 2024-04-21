# python3
import sys


def sort_char(s):
    alpha = ["$", "A", "C", "G", "T"]
    l_s = len(s)
    order = [0] * l_s
    count = [0] * len(alpha)
    for i in range(l_s):
        count[alpha.index(s[i])] = count[alpha.index(s[i])] + 1
    for j in range(1, len(alpha)):
        count[j] = count[j] + count[j-1]
    # print("count: {}".format(count))
    for i in reversed(range(l_s)):
        c = s[i]
        count[alpha.index(c)] -= 1
        order[count[alpha.index(c)]] = i
    print("string: {}, order: {}".format([*s], order))
    return order


def compute_char_class(s, order):
    l_s = len(s)
    cls = [0] * l_s
    cls[order[0]] = 0
    for i in range(1, l_s):
        if s[order[i]] != s[order[i-1]]:
            cls[order[i]] = cls[order[i-1]] + 1
        else:
            cls[order[i]] = cls[order[i - 1]]
    print("class: {}".format(cls))
    return cls


def sort_doubled(s, L, order, cls):
    l_s = len(s)
    count = [0] * l_s
    order_new = [0] * l_s
    for i in range(l_s):
        count[cls[i]] = count[cls[i]] + 1
    for j in range(1, l_s):
        count[j] = count[j] + count[j-1]
    for i in reversed(range(l_s)):
        start = (order[i] - L + l_s) % l_s
        cl = cls[start]
        count[cl] = count[cl] - 1
        order_new[count[cl]] = start
    return order_new


def update_class(order, cls, L):
    l_order = len(order)
    cls_new = [0] * l_order
    cls_new[order[0]] = 0
    for i in range(1, l_order):
        cur = order[i]
        prev = order[i-1]
        mid = cur + L
        mid_prev = (prev+L) % l_order
        if cls[cur] != cls[prev] or cls[mid] != cls[mid_prev]:
            cls_new[cur] = cls_new[prev] + 1
        else:
            cls_new[cur] = cls_new[prev]
    return cls_new


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    l_s = len(text)
    order = sort_char(text)
    cls = compute_char_class(text, order)
    L = 1
    while L < l_s:
        order = sort_doubled(text, L, order, cls)
        cls = update_class(order, cls, L)
        L *= 2
    # Implement this function yourself
    return order


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(" ".join(map(str, build_suffix_array(text))))
