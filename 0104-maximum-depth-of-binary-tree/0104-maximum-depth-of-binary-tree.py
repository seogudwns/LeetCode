# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        ans,bef,aft = 0,[root],[]
        while bef:
            while bef:
                node = bef.pop()
                if node.left: aft.append(node.left)
                if node.right: aft.append(node.right)
            bef,aft = aft,[]
            ans += 1

        return ans