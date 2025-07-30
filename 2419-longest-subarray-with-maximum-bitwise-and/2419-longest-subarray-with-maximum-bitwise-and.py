class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        mmax = max(nums)
        return max(len(list(values)) for key,values in groupby(nums) if key == mmax)