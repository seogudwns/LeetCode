from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            root = TreeNode(val=val,left = root)
            return root
        
        Q = deque([(root,1)]) # current, depth.
        while Q:
            node,dep = Q.popleft()
            
            if dep + 1 == depth:
                node.left = TreeNode(val=val,left=node.left)
                node.right = TreeNode(val=val,right=node.right)
            else:
                if node.left:
                    Q.append((node.left,dep+1))
                if node.right:
                    Q.append((node.right,dep+1))
                    
        return root