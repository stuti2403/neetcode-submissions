# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        l_d=self.maxDepth(root.left)
        r_d=self.maxDepth(root.right)
        d=max(l_d,r_d)+1
        return d