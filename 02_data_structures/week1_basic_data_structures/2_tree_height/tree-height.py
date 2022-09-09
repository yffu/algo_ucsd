# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size
debug = False

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))
                nodes = [[] for i in range(self.n)]  # child nodes of each node
                self.height = [0 for i in range(self.n)] # heights of each node
                for i in range(self.n):
                        p = self.parent[i]
                        if p == -1:
                                self.root = i
                        else:
                                nodes[p].append(i)
                self.nodes = nodes

        def compute_height(self):
                # Replace this code with a faster implementation
                if debug:
                        print('nodes: ' + str(self.nodes))
                        print('root index: ' + str(self.root))
                maxHeight = 0
                queue = [self.root]
                while queue:
                        n = queue.pop(0)
                        if self.parent[n] == -1:
                                self.height[n] = 1
                        else:
                                self.height[n] = self.height[self.parent[n]] + 1
                        queue.extend(self.nodes[n])
                return max(self.height)

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
