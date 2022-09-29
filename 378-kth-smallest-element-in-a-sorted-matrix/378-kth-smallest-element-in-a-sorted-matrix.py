# import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    
        
    
#         # second
        return sorted(sum(matrix,[]))[k-1]
    
#         # first
#         lst = []
#         for i in matrix:
#             for j in i:
#                 heapq.heappush(lst,j)
        
#         for _ in range(k-1):
#             heapq.heappop(lst)
            
#         return heapq.heappop(lst)