# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        Q,val = [root],[]
        
        while Q:
            x = Q.pop()
            heapq.heappush(val,x.val)
            if x.left: Q.append(x.left)
            if x.right: Q.append(x.right)
        
        curr = heapq.heappop(val)
        ans = float('inf')
        while val:
            nex = heapq.heappop(val)
            ans = min(ans,nex-curr)
            curr = nex
        
        return ans