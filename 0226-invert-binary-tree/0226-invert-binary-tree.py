# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        Q = deque([root])
        while Q:
            x = Q.popleft()
            if x.left and x.right: 
                x.left,x.right = x.right,x.left
                Q.append(x.left)
                Q.append(x.right)
            elif x.right:
                x.left,x.right = x.right,None
                Q.append(x.left)
            elif x.left:
                x.left,x.right = None,x.left
                Q.append(x.right)
        
        return root