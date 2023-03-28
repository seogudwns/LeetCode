class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        last = days[-1]
        chk,days = [0 for _ in range(last)],set(days)
        o,s,m = costs
        
        for i in range(last):
            if i not in days: chk[i] = chk[i-1]
            else: chk[i] = min(chk[i-1]+o,chk[max(0,i-7)]+s,chk[max(0,i-30)]+m)
                
        return chk[-1]
        
class Solution:
    def mincostTickets(self, days, costs):
    
        dp = [0] * 366
        travel_days = set(days)
        for i in range(1, 366):
            if i not in travel_days:
                dp[i] = dp[i-1]
            else:
                dp[i] = min(dp[i-1] + costs[0], dp[max(0, i-7)] + costs[1], dp[max(0, i-30)] + costs[2])
        return dp[365]