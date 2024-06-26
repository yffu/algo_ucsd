#Uses python3
import sys
import logging

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    # write your code here
    count_node = 0
    for pattern in patterns:
        current_node = 0
        for symbol in pattern:
            # logging.debug("i: {}, symbol: {}".format(current_node, symbol))
            if current_node in tree:
                if symbol in tree[current_node]:
                    current_node = tree[current_node][symbol]
                else:
                    count_node += 1
                    tree[current_node][symbol] = count_node
                    current_node = count_node
            else:
                count_node += 1
                tree[current_node] = dict()
                tree[current_node][symbol] = count_node
                current_node = count_node

            # logging.debug("trie: {}".format(tree))
    return tree


if __name__ == '__main__':
    # logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
