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
        
        Q = [(root,1)]
        while Q:
            curr,dep = Q.pop()
            
            if dep == depth-1:
                curr.left = TreeNode(val=val,left=curr.left)
                curr.right = TreeNode(val=val,right=curr.right)
                continue
            if curr.left:
                Q.append((curr.left,dep+1))
            if curr.right:
                Q.append((curr.right,dep+1))
        
        return root