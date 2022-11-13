# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
debug = False

class TreeOrders:
    def read(self):
        # read number of nodes from first line
        self.n = int(sys.stdin.readline())
        # initiate array of key, index of left child, index of right child
        self.key = [0 for i in range(self.n)]
        self.left = [0 for i in range(self.n)]
        self.right = [0 for i in range(self.n)]
        for i in range(self.n):
            [a, b, c] = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c
        if debug:
            print(self.key)
            print(self.left)
            print(self.right)


    def InOrderTraversal(self, tree):
        if tree == -1:
            return
        self.InOrderTraversal(self.left[tree])
        self.result.append(self.key[tree])
        self.InOrderTraversal(self.right[tree])


    def inOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.InOrderTraversal(0)
        return self.result


    def PreOrderTraversal(self, tree):
        if tree == -1:
            return
        self.result.append(self.key[tree])
        self.PreOrderTraversal(self.left[tree])
        self.PreOrderTraversal(self.right[tree])


    def preOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.PreOrderTraversal(0)
        return self.result

    def PostOrderTraversal(self, tree):
        if tree == -1:
            return
        self.PostOrderTraversal(self.left[tree])
        self.PostOrderTraversal(self.right[tree])
        self.result.append(self.key[tree])

    def postOrder(self):
        self.result = []
        # Finish the implementation
        # You may need to add a new recursive method to do that
        self.PostOrderTraversal(0)
        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))


threading.Thread(target=main).start()
