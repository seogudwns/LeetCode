class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        res = 0
        
        nums = sorted(nums)
        for i in range(1,len(nums)):
            if res < nums[i]-nums[i-1]:
                res = nums[i]-nums[i-1]
        
        return res