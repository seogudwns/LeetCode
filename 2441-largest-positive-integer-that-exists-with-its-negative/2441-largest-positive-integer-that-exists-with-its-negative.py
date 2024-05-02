class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums = set(nums)
        return max([i for i in nums if i>0 and -i in nums]+[-1])