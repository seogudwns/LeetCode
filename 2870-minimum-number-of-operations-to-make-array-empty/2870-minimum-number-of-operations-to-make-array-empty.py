class Solution:
    def minOperations(self, nums: List[int]) -> int:
        x= Counter(nums)
        return -1 if 1 in x.values() else sum((x[i]+2)//3 for i in set(nums))