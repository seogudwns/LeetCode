# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        nums = set()
        def last_sum(root,node):
            if targetSum in nums:
                return
            if not root.left and not root.right:
                nums.add(node+root.val)
                return
            
            if root.left:
                last_sum(root.left,node+root.val)
            if root.right:
                last_sum(root.right,node+root.val)
        
        last_sum(root,0)
        # print(nums)
        return targetSum in nums