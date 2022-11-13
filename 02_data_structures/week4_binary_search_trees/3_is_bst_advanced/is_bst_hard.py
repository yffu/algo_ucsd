#!/usr/bin/python3

import sys, threading
sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size
debug = False


class Solver:
    def __init__(self, tree):
        self.tree = tree

    def IsBinarySearchTree(self):
        # empty tree is bst
        if not self.tree:
            return True
        isBST, min, max = self.test_BST(0)
        return isBST

    def test_BST(self, i):
        # leaf node + 1, has no value, min or max
        if i == -1:
            return True, None, None
        val = self.tree[i][0]
        # recursive check left child, return largest element
        l, lmin, lmax = self.test_BST(self.tree[i][1])
        # recursive check right child, return smallest element
        r, rmin, rmax = self.test_BST(self.tree[i][2])
        if debug:
            print('i', i, 'val', val, sep=', ')
            print('lbool', l, 'lmax', lmax, 'lmin', lmin, sep=', ')
            print('rbool', r, 'rmax', rmax, 'rmin', rmin, sep=', ')
        # (val > lmax) and (val <= rmin)
        if not (l and r):
            return False, lmin, rmax
        # leaf node on l
        if not (lmin and lmax):
            lmin, lmax = val, val
        else:
            l = (val > lmax)
        # left node on r
        if not (rmin and rmax):
            rmin, rmax = val, val
        else:
            r = (val <= rmin)
        return (l and r), lmin, rmax


def main():
    nodes = int(sys.stdin.readline().strip())
    tree = []
    for i in range(nodes):
        tree.append(list(map(int, sys.stdin.readline().strip().split())))
    solver = Solver(tree)
    if solver.IsBinarySearchTree():
        print("CORRECT")
    else:
        print("INCORRECT")


threading.Thread(target=main).start()
