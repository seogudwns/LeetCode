# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        Q = [(root,1)]
        check1,check2 = 0,0
        while Q:
            x,cnt = Q.pop()
            check1 += 1
            check2 = max(check2,cnt)
            if x.left: Q.append((x.left,2*cnt))
            if x.right: Q.append((x.right,2*cnt+1))
        return check1 == check2