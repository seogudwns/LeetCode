from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        Q = deque([root])
        lst = []
        
        while Q:
            x = Q.popleft()
            lst.append(x.val)
            if x.left:
                Q.append(x.left)
            if x.right:
                Q.append(x.right)
        
        lst = sorted(lst)
        leng = len(lst)
        l,r = 0 , leng-1
        
        while l<r:
            num = lst[l]+lst[r]
            if num == k:
                return True
            elif num < k:
                l += 1
            elif num > k:
                r -= 1
        
        return False