class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        rot = [(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1),(-2,1),(-1,2)]
        
        @lru_cache(None)
        def knightcheck(ro,co,mo):
            if mo == k:
                return 1
            ans = 0
            for i,j in rot:
                nro,nco = ro+i,co+j
                if 0<=nro<n and 0<=nco<n:
                    ans+=1/8 * knightcheck(nco,nro,mo+1)
                        
            return ans
        
        return knightcheck(row,column,0)
        
#         prob = 8
#         ans = 1
#         for i in range(k):
#             ans -= N[i]/prob
#             prob*=8
        
#         return ans

# 8
# 30
# 6
# 4