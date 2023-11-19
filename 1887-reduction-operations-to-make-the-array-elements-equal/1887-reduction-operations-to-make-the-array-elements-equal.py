class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        x = Counter(nums)
        return sum(i*x[j] for i,j in enumerate(sorted(x)))