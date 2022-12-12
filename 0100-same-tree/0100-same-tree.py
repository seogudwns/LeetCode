# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p or not q:
            if not p and not q:
                return True
            
            return False
                
        try:
            Q = [(p,q)]
            while Q:
                x,y = Q.pop()
                if x.val != y.val:
                    return False
                
                if x.left or y.left:
                    Q.append((x.left,y.left))
                if x.right or y.right:
                    Q.append((x.right,y.right))                
            return True
        
        except:
            return False