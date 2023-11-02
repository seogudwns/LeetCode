# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def chk(self,node):
            val,cnt = node.val,1
            if node.left:
                x,y = self.chk(node.left)
                val += x
                cnt += y
            if node.right:
                x,y = self.chk(node.right)
                val += x
                cnt += y
            if node.val == int(val/cnt):
                self.ans += 1
            return val,cnt
    
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.chk(root)
        
        return self.ans