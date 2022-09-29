import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted(sum(matrix,[]))[k-1]
#         lst = []
#         for i in matrix:
#             for j in i:
#                 heapq.heappush(lst,j)
        
#         for _ in range(k-1):
#             heapq.heappop(lst)
            
#         return heapq.heappop(lst)