# natural.. 줄을 새우는 방법.
# target-n만큼의 공들 사이에 서로의 interval이 최대 k-1인 n-1개의 막대를 새우기.
# .
# .
# .

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if target<n or n*k<target:
            return 0
        
        leng = n*k+1
        dp = [0 for _ in range(leng)]
        for i in range(1,k+1):
            dp[i] = 1
        
        num = n
        while n != 1:
            # print(dp)
            dp_next = [0 for _ in range(leng)]
        
            for i in range(leng):
                if dp[i]:
                    for j in range(1,k+1):
                        dp_next[i+j] = (dp_next[i+j]+dp[i])%(1000000007)
                        
            
            n -= 1
            dp = dp_next
        
        # print(dp)
        return dp[target]