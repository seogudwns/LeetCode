class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = Counter(nums)
        return sum([i if nums[i] == 1 else 0 for i in nums])