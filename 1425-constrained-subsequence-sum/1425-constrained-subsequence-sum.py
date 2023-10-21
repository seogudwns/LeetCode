class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        # dp[i] = max sum of subseq(nums[:i+1]) s.t. j-i <= k
        # dp[i] = max(dp[j]) + nums[i] , j-i <= k
        
        n = len(nums)
        dp = [0 for i in range(n+1)]
        q = deque()
        res = -math.inf
        left = 1
        
        for i in range(1, n+1):
            prev_max = q[0] if q else 0
            dp[i] = max(prev_max, 0) + nums[i-1]    # if prev dp is neg, start new subsequence here
            res = max(res, dp[i])
            while q and dp[i] > q[-1]:
                q.pop()
            q.append(dp[i])
            
            if i - left >= k:
                if q[0] == dp[left]:
                    q.popleft()
                left += 1\
                       
        return res