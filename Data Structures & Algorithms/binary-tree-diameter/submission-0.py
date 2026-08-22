# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        dia=0
        def height(curr):
            nonlocal dia
            if curr is None:
                return 0
            l=height(curr.left)
            r=height(curr.right)
            dia=max(dia,l+r)
            return max(l,r)+1
        h=height(root)
        return dia
        