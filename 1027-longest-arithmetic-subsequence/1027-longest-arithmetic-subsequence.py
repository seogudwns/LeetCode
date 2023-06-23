class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return n

        longest = 2
        dp = [{} for _ in range(n)]

        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] = dp[j].get(diff, 1) + 1
                
        return max(max(i.values()) if i else 0 for i in dp)