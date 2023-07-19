class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) == 1: return 0
        nums = sorted(nums)
        return max(nums[i]-nums[i-1] for i in range(1,len(nums)))