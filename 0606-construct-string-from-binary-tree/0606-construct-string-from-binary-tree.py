# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        rootval = str(root.val)
        if root.right:
            if root.left:
                return f'{rootval}({self.tree2str(root.left)})({self.tree2str(root.right)})'
            return f'{rootval}()({self.tree2str(root.right)})'
        
        return rootval if not root.left else f'{rootval}({self.tree2str(root.left)})'