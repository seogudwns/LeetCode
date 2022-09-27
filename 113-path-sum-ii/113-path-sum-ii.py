# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root == None:
            return []
            
        results = []
        Q = deque([(root,targetSum,[])])
        
        while Q:
            node,res,lst = Q.popleft()
            if not (node.left or node.right):
                if node.val == res:
                    results.append(lst+[node.val])
                continue
            
            if node.left:
                Q.append((node.left,res-node.val,lst+[node.val]))
            if node.right:
                Q.append((node.right,res-node.val,lst+[node.val]))
            
        return results
        # res-node.val로 구분을 하기에는 음수인 케이스가 있기 때문에 불가능..!..
        
#         def seg(n,lst):
#             lst.append(n.val)
#             # print(lst)
#             # sum_lst = sum(lst)
#             # if sum_lst>targetSum:  
#             #     return   # 음수인 케이스가 있네..?..
            
#             if n.left or n.right:
#                 if n.left:
#                     seg(n.left,lst)
#                     lst.pop(-1)
                
#                 if n.right:
#                     seg(n.right,lst)
#                     lst.pop(-1)
                    
#             else:
#                 if sum(lst) == targetSum:
#                     result.append(lst.copy())
#                 return
            
#             return
        
#         seg(root,[])
        
#         return result
            