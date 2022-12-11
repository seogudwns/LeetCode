# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        nums = set()
        def dfs(node):
            if not node:
                return 0
            
            res = node.val
            l,r = dfs(node.left),dfs(node.right)
            nums.add(res)
            nums.add(res+l)
            nums.add(res+r)
            nums.add(res+l+r)
            return max(res,res+l,res+r)
        
        dfs(root)
        
        return max(nums)