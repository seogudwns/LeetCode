class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        for i in range(len(coins)):
            for j in range(i,amount+1):
                if j>=coins[i]: dp[j]+=dp[j-coins[i]]
        
        return dp[-1]
        
        
        
# #         TLE
#         n,coins = len(coins),sorted(coins)
        
#         @lru_cache(None)
#         def chk(bef,idx,curr):
#             if bef>idx: return 0
#             if curr == coins[idx]: return 1
#             if curr < coins[idx]: return 0
#             return sum(chk(idx,i,curr-coins[idx]) for i in range(idx,n))
        
#         return sum(chk(-1,i,amount) for i in range(n)) if amount else 1