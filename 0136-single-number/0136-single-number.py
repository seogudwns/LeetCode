class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        X = Counter(nums)
        for i in X:
            if X[i] == 1:
                return i