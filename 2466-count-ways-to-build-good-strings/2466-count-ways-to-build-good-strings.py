class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp,mod = [0]*(high+1),10**9+7
        dp[zero]+=1
        dp[one]+=1
        for i in range(min(zero,one)+1,high+1):
            dp[i]=(dp[i]+dp[i-zero]+dp[i-one])%mod
        # print(dp,dp[low:high+2])
        return sum(dp[low:high+2])%mod
        