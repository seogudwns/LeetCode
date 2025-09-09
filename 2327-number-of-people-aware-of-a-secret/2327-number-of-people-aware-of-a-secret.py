from collections import deque

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        # MOD = 10**9+7
        # knowns = deque([0]*(forget-delay))
        # delay = deque([0]*(delay-1)) # delay일동안 잠복.
        # delay.append(1)
        # tk = 0 # sum(knowns) : 알리는 사람 수.
        # ans = 1
        # # print(knowns,delay,ans)
        # for i in range(n-1):
        #     knowns.append(delay.popleft())
        #     fotgot = knowns[0]
        #     tk = (tk-knowns.popleft() + knowns[-1])%MOD
        #     delay.append(tk)
        #     ans = (ans+tk-fotgot)%MOD
        #     # print(knowns,delay,tk,ans)

        # return ans
        dp = [0]*n
        dp[0] = 1
        s,MOD = 0,10**9+7
        for i in range(delay,n):
            s = (s+dp[i-delay])%MOD
            dp[i] = s
            if i >= forget-1:
                s -= dp[i-forget+1]
        
        return(sum(dp[-forget:]))%MOD