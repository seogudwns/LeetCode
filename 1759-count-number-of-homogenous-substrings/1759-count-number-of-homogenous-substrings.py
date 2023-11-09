class Solution:
    def countHomogenous(self, s: str) -> int:
        ans,MOD = 0,10**9+7
        curr,bef = 1,s[0]
        for i in range(1,len(s)):
            if s[i] == bef:
                curr += 1
            else:
                ans = (ans+(curr*(curr+1))//2)%MOD
                curr,bef = 1,s[i]
        
        return (ans+(curr*(curr+1))//2)%MOD
                