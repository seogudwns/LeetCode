# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        ans,Q = 0,deque([root])
        while Q:
            curr = Q.pop()
            if curr.left:
                if not curr.left.left and not curr.left.right:
                    ans += curr.left.val
                else:
                    Q.append(curr.left)
            if curr.right:
                Q.append(curr.right)
        
        return ans