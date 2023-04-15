class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        
        n = len(piles)
            
        prefix = []
        
        #prev array represents where the elements from last pile ended
        prev = [0]
        
        for pile in piles:
            curr = [0]
            for ele in pile:
                curr.append(curr[-1]+ele)
            prefix.append(curr)
            
            prev.append(prev[-1]+len(pile))
            
        dp = [[0]*(k+1) for i in range(prev[-1]+1)]
            
        for i in range(n):
            for j in range(1, len(prefix[i])):
                
                profit = prefix[i][j]
                wt = j

                # lvl represents row number
                # We've given a different row to every prefix sum array element.   
                lvl = prev[i]+j 
                
                for w in range(1, k+1): 
                    if wt > w:
                        dp[lvl][w] = dp[lvl-1][w]
                    else:
                        dp[lvl][w] = max(dp[lvl-1][w], profit+dp[prev[i]][w-wt])
        return dp[-1][-1]