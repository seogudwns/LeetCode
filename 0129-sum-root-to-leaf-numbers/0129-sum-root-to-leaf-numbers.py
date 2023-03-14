# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        Q,ans = deque([(root,0)]),0
        while Q:
            curr,val = Q.popleft()
            val += curr.val
            if curr.left or curr.right:
                if curr.left: Q.append((curr.left,val*10))
                if curr.right: Q.append((curr.right,val*10))
            else: ans += val
        
        return ans