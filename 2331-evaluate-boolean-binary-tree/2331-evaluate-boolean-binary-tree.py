# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def chk(node): return node.val == 1 if node.val < 2 else chk(node.left) or chk(node.right) if node.val == 2 else chk(node.left) and chk(node.right)
        
        return chk(root)