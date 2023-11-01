# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        x = Counter()
        ans,comp ={root.val},1
        Q = [root]
        
        while Q:
            y = Q.pop()
            x[y.val]+=1
            if y.left: Q.append(y.left)
            if y.right: Q.append(y.right)
        
        for i in x:
            if x[i]==comp: ans.add(i)
            elif x[i]>comp: 
                ans = {i}
                comp = x[i]
                
        return ans