import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lst = []
        for i in matrix:
            for j in i:
                if len(lst)<k:
                    heapq.heappush(lst,-j)
                elif -lst[0]>j:
                    heapq.heappop(lst)
                    heapq.heappush(lst,-j)
        
        print(lst)
        return -lst[0]
                    
#         # second
#         return sorted(sum(matrix,[]))[k-1]
    
#         # first
#         lst = []
#         for i in matrix:
#             for j in i:
#                 heapq.heappush(lst,j)
        
#         for _ in range(k-1):
#             heapq.heappop(lst)
            
#         return heapq.heappop(lst)