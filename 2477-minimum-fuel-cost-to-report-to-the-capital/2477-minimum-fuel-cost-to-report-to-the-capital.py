class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        n = len(roads)+1
        gp,dp = [[] for _ in range(n)],[0 for _ in range(n)]
        for i,j in roads:
            gp[i].append(j)
            gp[j].append(i)
                
        def dfs(par,curr):
            val = 1
            for i in gp[curr]: 
                if i == par: continue
                val += dfs(curr,i)
            
            dp[curr] = val
            return val
        
        dfs(-1,0)
        
        return sum(ceil(dp[i]/seats) for i in range(1,n))