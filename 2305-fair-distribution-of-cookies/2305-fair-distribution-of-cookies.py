class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        dp = [[-1] * (1 << n) for _ in range(k + 1)]
        
        def unfairness(k, bagMask):
            if dp[k][bagMask] != -1: 
                return dp[k][bagMask]
            
            def sum_cookies(Mask):
                return sum(cookies[i] if Mask&(1<<i) else 0 for i in range(n))
            
            # end of  sum_cookies 
            if k==1:
                dp[k][bagMask] = sum_cookies(bagMask)
                return dp[k][bagMask]
            ans=2**31
            Mask=bagMask
            while(Mask>0):
                sum1=sum_cookies(Mask)
                sum2=unfairness(k - 1, bagMask ^ Mask)
                ans=min(ans, max(sum1, sum2))
                Mask=(Mask - 1) & bagMask
            dp[k][bagMask] = ans
            return ans
        # end of unfairness
        return unfairness(k, (1 << n) - 1)