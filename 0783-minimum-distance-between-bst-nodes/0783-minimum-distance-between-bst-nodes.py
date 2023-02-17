# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        lst = set()
        Q = deque([root])
        while Q:
            x = Q.pop()
            if x.val in lst: return 0
            lst.add(x.val)
            if x.left: Q.append(x.left)
            if x.right: Q.append(x.right)
        
        lst = sorted(lst)
        return min(lst[i]-lst[i-1] for i in range(1,len(lst)))