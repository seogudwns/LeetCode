class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        x = Counter(nums)
        return sum((x[i]*(x[i]-1))//2 for i in x)