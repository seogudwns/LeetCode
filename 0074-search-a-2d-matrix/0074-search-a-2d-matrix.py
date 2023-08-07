# before solution.
# class Solution:
#     def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#         n = len(matrix)
#         x = 0
#         for i in range(n):
#             if matrix[i][0] > target:
#                 x = i-1
#                 break
#             elif matrix[i][0] == target:
#                 return True
#         if matrix[i][0] < target:
#             x = i
        
#         if x == -1:
#             return False
        
#         return target in matrix[x]

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n,m = len(matrix),len(matrix[0])
        l,r = 0,n*m-1
        
        while l<=r:
            mid = (l+r)//2
            h,v = divmod(mid,m)
            if matrix[h][v] == target: return True
            elif matrix[h][v] < target: l = mid+1
            else: r = mid-1
        
        return False