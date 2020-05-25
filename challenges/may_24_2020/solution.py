from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        root = TreeNode(preorder.pop(0))
        while len(preorder):
            val = preorder.pop(0)
            temp = root
            _t = temp
            while temp:
                _t = temp
                if val < temp.val:
                    temp = temp.left
                else:
                    temp = temp.right
            if val < _t.val:
                _t.left = TreeNode(val)
            else:
                _t.right = TreeNode(val)
        return root


s = Solution()
s.bstFromPreorder([8, 5, 1, 7, 10, 12])
