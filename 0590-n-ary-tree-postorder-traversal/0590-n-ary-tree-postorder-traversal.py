"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return []
        res = []
        def recur(x):
            for i in x.children:
                recur(i)
            nonlocal res
            res.append(x.val)
            
        
        recur(root)
        
        return res
        