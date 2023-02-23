class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profits = sorted(zip(capital,profits),key=lambda x: (-x[0],x[1]))
        capital.clear()
        while True:
            if k == 0: break
            
            while profits and profits[-1][0] <= w: heapq.heappush(capital,-profits.pop()[1])
            
            if not capital: break
            w -= heapq.heappop(capital)
            k -= 1
        
        return w
            
#         # 첫+ 풀이.. TLE
#         maxi = []
        
#         dic = defaultdict(list)
#         for i in range(len(profits)): dic[capital[i]].append(-profits[i])
            
#         dic = dict(dic)

#         for i in range(w+1): 
#             if i in dic:
#                 maxi += dic[i]
#                 del dic[i]
                
#         heapq.heapify(maxi)
        
#         for _ in range(k):
#             if not maxi: break
            
#             x = -heapq.heappop(maxi)
#             for i in range(w+1,w+x+1): 
#                 if i in dic:
#                     maxi += dic[i]
#                     del dic[i]
#             heapq.heapify(maxi)
            
#             w += x
            
#         return w