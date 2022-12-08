# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 or not root2:
            if not root1 and root2:
                return True
            return False
        
        Q = deque([root1])
        res1 = []
        while Q:
            x = Q.pop()
            if x.right or x.left:
                if x.right:
                    Q.append(x.right)
                if x.left:
                    Q.append(x.left)
            else:
                res1.append(x.val)
        
        Q.append(root2)
        res2 = []
        while Q:
            x = Q.pop()
            if x.right or x.left:
                if x.right:
                    Q.append(x.right)
                if x.left:
                    Q.append(x.left)
            else:
                res2.append(x.val)
                
        return res1 == res2