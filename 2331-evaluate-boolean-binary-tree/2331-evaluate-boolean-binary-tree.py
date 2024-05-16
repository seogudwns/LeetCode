# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == 1 if root.val < 2 else self.evaluateTree(root.left) or self.evaluateTree(root.right) if root.val == 2 else self.evaluateTree(root.left) and self.evaluateTree(root.right)
#         def chk(node): return node.val == 1 if node.val < 2 else chk(node.left) or chk(node.right) if node.val == 2 else chk(node.left) and chk(node.right)
        
#         return chk(root)