# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        Q = deque([root])
        while Q:
            x = Q.popleft()
            if x.left:
                Q.append(x.left)
            if x.right:
                Q.append(x.right)
            
            if low<=x.val<=high:
                res += x.val
        
        return res