class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        x = Counter(i for i in nums if not i%2)
        if not x:
            return -1
        return max(x,key = lambda y:(x[y],-y))