# 1 2 5 11 24 53

class Solution:
    def numTilings(self, n: int) -> int:
        div = 10**9+7
        dp = [0,1,2,5]
        if n<4: return dp[n]
        for i in range(n-3):
            dp.append((2*dp[-1]+dp[-3])%div)
        
        # print(dp)
        return dp[-1]