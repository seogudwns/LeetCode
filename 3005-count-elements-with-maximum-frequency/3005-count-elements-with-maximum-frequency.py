class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        x = Counter(nums)
        return max(x.values())*len([i for i in x if x[i] == max(x.values())])