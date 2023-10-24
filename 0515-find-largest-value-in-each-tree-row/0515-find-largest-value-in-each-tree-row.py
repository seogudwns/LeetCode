# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        ans = []
        Q = deque([(1,root)])
        while Q:
            dep,curr = Q.pop()
            if len(ans)<dep: ans.append(-float('inf'))
            ans[dep-1] = max(ans[dep-1],curr.val)
            if curr.left: Q.append((dep+1,curr.left))
            if curr.right: Q.append((dep+1,curr.right))
        
        return ans