class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        temp = root
        stack = []  # For InOrder Traversal LDR
        traversed = [None]
        while True:
            if temp:
                stack.append(temp)
                temp = temp.left
            elif stack:
                temp = stack.pop()
                traversed.append(temp.val)
                temp = temp.right
            else:
                break
        return traversed[k]


s = Solution()
r1 = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(s.kthSmallest(r1, 2))
r2 = TreeNode(5, TreeNode(3, TreeNode(
    2, TreeNode(1)), TreeNode(4)), TreeNode(6))
print(s.kthSmallest(r2, 3))
