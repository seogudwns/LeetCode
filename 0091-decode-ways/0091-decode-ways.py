class Solution:
    def numDecodings(self, s: str) -> int:
        n,dp = len(s),[0 for _ in range(len(s)+2)]
        dp[n] = 1
        for i in range(n-1,-1,-1):
            if s[i] == '0':
                dp[i] = 0
            else:
                dp[i] +=dp[i+1]
            if s[i] == '1' or (i != n-1 and s[i] == '2' and s[i+1] in '0123456'):
                dp[i] += dp[i+2]
        return dp[0]