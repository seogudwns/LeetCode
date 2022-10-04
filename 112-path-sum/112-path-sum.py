from collections import deque

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
        
#         nums = set()
#         def last_sum(root,node):
#             if targetSum in nums:
#                 return
#             if not root.left and not root.right:
#                 nums.add(node+root.val)
#                 return
            
#             if root.left:
#                 last_sum(root.left,node+root.val)
#             if root.right:
#                 last_sum(root.right,node+root.val)
        
#         last_sum(root,0)
#         # print(nums)
#         return targetSum in nums
        Q = deque([(0,root)])
        while Q:
            val,tree = Q.popleft()
            val += tree.val
            if not tree.left and not tree.right:
                if val == targetSum:
                    return True
                continue
            
            if tree.left:
                Q.append((val,tree.left))
            if tree.right:
                Q.append((val,tree.right))
        
        return False