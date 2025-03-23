class TreeNode:
def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class LeafIterator:
    def __init__(self, root):
        self.stack = []
        self.stack.append(root)

    def get_leaf(self):
        while self.stack:
            n = self.stack.pop()
            if (not (n.left or n.right)):
                return (n.val)
            else:
                if (n.right):
                    self.stack.append(n.right)
                if (n.left):
                    self.stack.append(n.left)
        return None


class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        li1 = LeafIterator(root1)
        li2 = LeafIterator(root2)
        while True:
            n1 = li1.get_leaf()
            n2 = li2.get_leaf()
            if (not (n1 or n2)):
                return True
            elif (n1 != n2):
                return False


if __name__ == '__main__':
    s = Solution()
