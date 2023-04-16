class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        n,m = len(words[0]),len(target)
        mod,dp = 10**9+7,[0 for _ in range(m+1)]
        dp[0] = 1
        
        cnt = [[0] * 26 for _ in range(n)]
        for i in range(n):
            for j in words:
                cnt[i][ord(j[i]) - 97] += 1
        
        for i in range(n):
            for j in range(m-1, -1, -1):
                dp[j+1] += dp[j] * cnt[i][ord(target[j]) - 97]
                dp[j+1] %= mod
        
        return dp[m]