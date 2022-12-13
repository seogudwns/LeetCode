class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        for i in range(1,n):
            for j in range(n):
                matrix[i][j] += min(matrix[i-1][max(0,j-1):min(n,j+2)])
        
        return min(matrix[-1])
        
#         # TLE..
#         n = len(matrix)
#         res = float('inf')
#         def check(val,ro,co):
#             if co == n:
#                 nonlocal res
#                 res = min(res,val)
#                 return
            
#             for i in range(max(0,ro-1),min(n,ro+2)):
#                 check(val+matrix[co][i],i,co+1)
        
#         for i in range(n):
#             check(matrix[0][i],i,1)
            
#         return res