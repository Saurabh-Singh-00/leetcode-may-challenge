import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = [root]
        depth = collections.defaultdict(lambda: 0)
        parent = collections.defaultdict(lambda: 0)
        depth[root.val] = 0

        while len(q):
            n = q.pop(0)
            if n.left:
                if n.left.val:
                    depth[n.left.val] = 1 + depth[n.val]
                    parent[n.left.val] = n.val
                q.append(n.left)
            if n.right:
                if n.right.val:
                    depth[n.right.val] = 1 + depth[n.val]
                    parent[n.right.val] = n.val
                q.append(n.right)
            if depth[x] and depth[y]:
                break

        if (depth[x] == depth[y]) and (parent[x] != parent[y]):
            return True
        return False


r1 = TreeNode(1, left=TreeNode(2, None, TreeNode(4)),
              right=TreeNode(3, None, TreeNode(5)))
r2 = TreeNode(1, left=TreeNode(2, TreeNode(4)), right=TreeNode(3))
r3 = TreeNode(1, left=TreeNode(2, None, TreeNode(4)), right=TreeNode(3))
s = Solution()
print(s.isCousins(r1, 5, 4))
print(s.isCousins(r2, 4, 3))
print(s.isCousins(r3, 2, 3))
