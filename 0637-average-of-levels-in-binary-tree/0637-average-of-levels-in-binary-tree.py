# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        
        Q = deque([(root,1,root.val)])
        res = []
        while Q:
            r,dep,val = Q.popleft()
            if len(res)<dep:
                res.append([])
            res[dep-1].append(val)
            if r.left:
                Q.append((r.left,dep+1,r.left.val))
            if r.right:
                Q.append((r.right,dep+1,r.right.val))
        
        return [sum(i)/len(i) for i in res]