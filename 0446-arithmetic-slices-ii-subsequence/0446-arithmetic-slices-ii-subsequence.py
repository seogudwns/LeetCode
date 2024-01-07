class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp = [defaultdict(int) for _ in range(len(nums))]
        res = 0
        for i in range(1,len(nums)):
            for j in range(i):
                dif = nums[i]-nums[j]
                if dif in dp[j]: res += dp[j][dif]
                dp[i][dif] += dp[j][dif]+1
                
        return res