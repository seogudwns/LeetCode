# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res = [-10**7]*200
        Q = [(0,root)]
        while Q:
            dep,curr = Q.pop()
            if res[dep] == -10**7: res[dep] = 0
            res[dep]+=curr.val
            if curr.left: Q.append((dep+1,curr.left))
            if curr.right: Q.append((dep+1,curr.right))

        return res.index(max(res))+1