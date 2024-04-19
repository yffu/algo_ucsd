# python3
import sys


def compute_prefix(p):
    l_p = len(p)
    s = [0] * l_p
    border = 0
    for i in range(1, l_p):
        while (border > 0) and (p[i] != p[border]):
            border = s[border - 1]
        if p[i] == p[border]:
            border += 1
        else:
            border = 0
        s[i] = border
    return s


def find_pattern(pattern, text):
    """Find all the occurrences of the pattern in the text
    and return a list of all positions in the text
    where the pattern starts in the text.
    """
    s = pattern + "$" + text
    prefix_func = compute_prefix(s)
    # print("pattern: {}, text: {}".format(pattern, text))
    # print("prefix_func: {}".format(prefix_func))
    l_p = len(pattern)
    result = []
    for i in range(l_p + 1, len(s)):
        # print("i: {}".format(i))
        if prefix_func[i] == l_p:
            result.append(i-2*l_p)
    # Implement this function yourself
    return result


if __name__ == '__main__':
    pattern = sys.stdin.readline().strip()
    text = sys.stdin.readline().strip()
    result = find_pattern(pattern, text)
    print(" ".join(map(str, result)))

