"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        def recur(x):
            nonlocal res
            res.append(x.val)
            for i in x.children:
                recur(i)
            
        
        recur(root)
        
        return res