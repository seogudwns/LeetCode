class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        dp = [0 for _ in prices]
        # [1,2,6,0,8,10] --> [0,1,5,5,9,11,11,12]
#         last_idx, last_val, last_val_bef, curr_val, curr_val_bef = 0,0,0,0,0
#         cnt = 0
#         start = 0
#         for i in range(1,len(prices)):
#             if prices[i-1]<=prices[i]:
#                 if cnt == 0:
#                     start = prices[i-1]
#                 cnt += 1
#                 last_val_bef = last_val
#                 last_val = prices[i]-start
#                 dp[i] = last_val
            
#             else: # down the price.
#                 dp[i] = dp[i-1]
#                 cnt = 0
#                 start = 0
        n = len(prices)
        b = [0] * n
        s = [0] * n
        b[0] = -prices[0]
        for i in range(1, len(prices)):
            b[i] = max(b[i - 1], s[i - 2] - prices[i])
            s[i] = max(s[i - 1], b[i - 1] + prices[i])
        return s[-1]
        
                
        
        
        
        return dp[-1]