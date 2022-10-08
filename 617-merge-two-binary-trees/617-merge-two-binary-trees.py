from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1 or not root2:
            if not root1:
                return root2
            if not root2:
                return root1
            return []
        Q = deque([(root1,root2)])
        while Q:
            l,r = Q.popleft()
            if r:
                l.val += r.val
            
            if l.left and r.left:
                Q.append((l.left,r.left))
            elif r.left:
                l.left = r.left
            
            if l.right and r.right:
                Q.append((l.right,r.right))
            elif r.right:
                l.right = r.right
        
        return root1