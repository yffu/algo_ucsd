debug = False


def binary_search(keys, query):
    # write your code here
    if debug:
        print("keys: " + str(keys))
        print("query: " + str(query))

    # Attempt 1
    '''
    if query < keys[0] or query > keys[len(keys)-1]:
        if debug: print("out of bounds ")
        return -1
    offset = 0
    while keys:
        # pre-condition len(keys) = n, n >= 1
        # take middle value
        # if n is odd, take mid = n//2; n = 1, mid = 0; n = 3, mid = 1
        # if n is even, take mid = n//2; n = 2, mid = 1; n = 4, mid = 2
        hi = keys[len(keys)-1]
        lo = keys[0]
        mid = len(keys)//2
        if debug: print("mid: " + str(mid) + " with value: " + str(keys[mid]))
        if query == keys[mid]:
            return mid + offset
        elif query < keys[mid]:
            keys = keys[:mid]
        elif query > keys[mid]:
            keys = keys[mid+1:]
            offset += (mid+1)
        if debug: print("keys: " + str(keys))
    return -1
    '''

    #Attempt 2
    left = 0
    right = len(keys)
    while left != right:
        if query < keys[left] or query > keys[right-1]:
            return -1
        mid = (left + right)//2
        m_val = keys[mid]
        if debug:
            print()
            print("left: " + str(left) + " mid: " + str(mid) + " right: " + str(right))
        # base case:
        # left = 0, right = 1 mid = 0,
        # left = 0, right = 2 mid = 1,
        # left = 0, right = 3 mid = 1
        if left == mid:
            if debug:
                print("is a base case")
                print("mid: " + str(mid) + " with val: " + str(m_val) + " query: " + str(query))
            return mid if query == m_val else -1
        else:
            if debug:
                print("not a base case")
                print("mid: " + str(mid) + " with val: " + str(m_val) + " query: " + str(query))
            if query == m_val:
                if debug: print("query == m_val")
                return mid
            elif query < m_val:
                if debug: print("query < m_val")
                right = mid
            elif query > m_val:
                if debug: print("query > m_val")
                left = mid + 1


if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
