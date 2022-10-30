class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(Counter(nums))