class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
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
        cap_pro = sorted(zip(capital,profits),key=lambda x: (-x[0],x[1]))
        candid = []
        while True:
            if k == 0: break
            
            while cap_pro and cap_pro[-1][0] <= w: heapq.heappush(candid,-cap_pro.pop()[1])
            
            if not candid: break
            w -= heapq.heappop(candid)
            k -= 1
        
        return w
            