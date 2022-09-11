# python3

debug = False


def sift_down(index, data, swaps):
    m_index = index
    l_child = index * 2 + 1
    r_child = index * 2 + 2
    if debug:
        print('l_child i: ' + str(l_child))
        print('r_child i: ' + str(r_child))
    if l_child < len(data) and data[l_child] < data[m_index]:
        m_index = l_child
    if r_child < len(data) and data[r_child] < data[m_index]:
        m_index = r_child
    if debug:
        print('m_index: ' + str(m_index) + ' index: ' + str(index))
    if m_index != index:
        data[index], data[m_index] = data[m_index], data[index]
        swaps.append([index, m_index])
        sift_down(m_index, data, swaps)


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    start from floor of n/2, as everything after is a leaf node.
    """
    swaps = []
    n = len(data)//2

    while n:
        if debug:
            print('n: ' + str(n))
        sift_down(n-1, data, swaps)
        n -= 1
    return swaps


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
