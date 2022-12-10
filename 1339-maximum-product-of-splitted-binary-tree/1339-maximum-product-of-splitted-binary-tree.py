# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0

            res = node.val+dfs(node.left)+dfs(node.right)
            nodeSums.add(res)

            return res

        nodeSums = set()
        treeSum = dfs(root)
        
        n = min(nodeSums,key = lambda x: abs(x-treeSum/2))
        
        return n*abs(n-treeSum)%1000000007 