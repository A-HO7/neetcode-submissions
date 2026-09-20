# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root :
            return True
        leftH = self.maxHeight(root.left)
        rightH = self.maxHeight(root.right)
        if abs(leftH-rightH) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        else :
            return False


    def maxHeight(self, root: Optional[TreeNode]) :
        if not root :
            return 0
        return 1 + max(self.maxHeight(root.left),self.maxHeight(root.right))