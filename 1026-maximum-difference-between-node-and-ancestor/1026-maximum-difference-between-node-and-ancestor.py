# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = 0
        
        Q = deque([(root,root.val,root.val)])
        while Q:
            x,maxi,mini = Q.popleft()
            
            if not x.right and not x.left:
                res = max(res,maxi-mini)
                continue
                
            if x.left:
                Q.append((x.left,max(maxi,x.left.val),min(mini,x.left.val)))
                
            if x.right:
                Q.append((x.right,max(maxi,x.right.val),min(mini,x.right.val)))
        
        return res