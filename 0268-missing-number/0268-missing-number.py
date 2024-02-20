class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for k,v in enumerate(sorted(nums)):
            if k != v:
                return k
        return len(nums)