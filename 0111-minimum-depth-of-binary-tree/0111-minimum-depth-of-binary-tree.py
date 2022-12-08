# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        Q = deque([(root,1)])
        while Q:
            x,dep = Q.popleft()
            if not x.left and not x.right:
                return dep
            
            if x.left:
                Q.append((x.left,dep+1))
            if x.right:
                Q.append((x.right,dep+1))