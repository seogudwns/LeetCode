"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        
        node_dict = dict()
        def levelOrd(root, level):
            if not root:
                return
            if level not in node_dict:
                node_dict[level] = []
            
            node_dict[level].append(root)
        
            levelOrd(root.left, level+1)
            levelOrd(root.right, level+1)
        
        levelOrd(root, 0)
        print(node_dict)
        
        last = 2
        for i in range(1,len(node_dict)):
            for j in range(0,last-1):
                node_dict[i][j].next = node_dict[i][j+1]
            last *= 2
        return root