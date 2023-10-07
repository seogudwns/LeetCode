class Solution:
    @lru_cache(None)
    def numOfArrays(self, n: int, m: int, k: int, curmax = -1) -> int:
        mod = 10**9+7
        
        if k > m: return 0 # cannot have increasing prefix of len K
        
        if n == 0:
            return int(k==0)
        if k < 0: 
            return 0
        
        
        # otherwise value can be any
        ways = 0
        for pick in range(1,m+1):
            cost = int(pick > curmax)
            ways += self.numOfArrays(n-1, m, k-cost, max(pick, curmax))
            ways %= mod
        
        return ways