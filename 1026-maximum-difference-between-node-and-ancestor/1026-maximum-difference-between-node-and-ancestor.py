# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        Q = deque([(root,[])])
        while Q:
            x,lines = Q.popleft()
            
            curr = x.val
            for i in lines:
                res = max(res,abs(i-curr))
                
            if x.left:
                Q.append((x.left,lines+[curr]))
                
            if x.right:
                Q.append((x.right,lines+[curr]))
        
        return res