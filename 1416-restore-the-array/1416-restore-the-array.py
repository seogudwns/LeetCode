class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n,m,M = len(s),len(str(k)),10**9+7
        dp = [0]*(n+1)
        dp[-1] = 1
        for i in range(n-1,-1,-1):
            if s[i] =='0': continue
            curr,tmp = 1,0
            for j in range(i+1,min(n+1,i+m+1)):
                if int(s[i:j])<=k: tmp = (tmp+dp[j])%M
            dp[i] = curr*tmp
            
        return dp[0]
        
        