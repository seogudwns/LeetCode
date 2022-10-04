

class Solution:
    def deleteString(self, s: str) -> int:
        if len(set(s)) == 1:
            return len(s)
        
        leng = len(s)
        dp = [0 for _ in range(leng)]
        leng2 = len(s)
        dp[0] = 1 # 한번에 없앨 수 있는 케이스.
        
        for i in range(leng):
            if not dp[i]: 
                continue
                
            sc = s[i:]
                
            for j in range(1,leng2//2+1):
                if sc[:2*j] == sc[:j]*2:
                    # print(sc,sc[:2*j])
                    dp[i+j] = max(dp[i]+1,dp[j])
                    # dp[-1] = max(dp[i+j],dp[-1])
        # print(dp)
        
        return max(dp)