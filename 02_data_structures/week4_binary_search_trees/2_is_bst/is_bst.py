# python3

import sys, threading
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
debug = False

# Testing the binary search tree condition for each node and every other node in its subtree will be too slow.
# You should come up with a faster algorithm.

def IsBinarySearchTree(tree):
    # Implement correct algorithm here
    if not tree:
        return True
    result = []
    InOrderTraversal(result, tree, 0)
    if debug:
        print('tree', tree, sep=': ')
        print('in order', result, sep=': ')
    for i in range(1, len(result)):
        if result[i-1] >= result[i]:
            return False
    return True


def InOrderTraversal(result, tree, i):
    if i == -1:
        return True
    InOrderTraversal(result, tree, tree[i][1])
    if debug:
        print('key', tree[i][0], sep=': ')
    result.append(tree[i][0])
    InOrderTraversal(result, tree, tree[i][2])


def main():
    # read number of nodes in first line
    nodes = int(sys.stdin.readline().strip())
    tree = []
    # read in each subsequent line for node information: key, index of left child, index of right child
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    if IsBinarySearchTree(tree):
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
